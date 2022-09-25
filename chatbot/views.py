from django import http
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from . import models

from linebot import LineBotApi, WebhookParser
from linebot.models import (
    Message,
    TextSendMessage, 
    TemplateSendMessage, 

    MessageEvent,
    PostbackEvent,
)

import requests as rq


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

bot_description = """
WarmCom，全稱為 Warm Company 有溫暖陪伴的意思，同時也諧音 Warm Come 表示溫暖來臨之意。

WarmCom 提供這些服務：
1. 發表文章：以匿名的方式發表文章
2. 給予溫暖：查看別人的文章並溫暖地回應對方
3. 收到溫暖：查看所收到來自他人的溫暖
4. 配對諮商：協助您找到適合的諮商師
5. 成為諮商師：若您願意諮商他人，則可填寫諮商資訊，並開啟配對功能
""".split("\n")[1:]
bot_description = "\n".join(bot_description)

@csrf_exempt
def receive_message(request):
    global pre_message
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')
    events = parser.parse(body, signature)
    for event in events:
        if isinstance(event, MessageEvent):
            if event.message.text == "這個機器人是做什麼的?":
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=bot_description))
        if isinstance(event, PostbackEvent):
            user_id = event.source.user_id
            data = resolve_postback_data(event.postback.data)
            action = data["action"]
            if action == "pair":
                send_message(user_id, "已發送邀請給該諮商師，等待回覆中...")
                rq.post(
                    f"{settings.BASE_DOMAIN}/api/appoint",
                    {
                        "user_id" : user_id,
                        "counselor_id" : data["counselor_id"],
                    }
                )
            if action == "help":
                send_message(user_id, "已接受，將您的 id 傳送給對方")
                rq.post(
                    f"{settings.BASE_DOMAIN}/api/help",
                    {
                        "user_id" : data["target_id"],
                        "counselor_id" : user_id,
                    }
                )

    return http.HttpResponse()


def resolve_postback_data(postback_data: str):
    result = {}
    for tmp in postback_data.split("&"):
        t = tmp.split("=")
        result[t[0]] = t[1]
    return result

def send_to_user(user_id: str, message: Message):
    line_bot_api.push_message(user_id, message)

def send_message(user_id: str, message: str):
    msg = TextSendMessage(text=message)
    send_to_user(user_id, msg)

def generate_counselors_information_template(filter_types: list):
    def generate_counselor_template(counselor: models.Counselor):
        gender = counselor.gender
        age = counselor.age
        job = counselor.job
        is_professional = counselor.is_professional

        title = counselor.user_name
        if len(gender) == 1 or age or is_professional:
            tmp = ""
            if len(gender) == 1:
                tmp += gender
            if age:
                if tmp:
                    tmp += "，"
                tmp += str(age)
            if tmp:
                tmp += "，"
            if is_professional:
                tmp += "專業"
            else:
                tmp += "非專業"
            title += f" ({tmp})"
        
        text = counselor.description
        if job:
            text = f"職業: {job}\n{text}"
        else:
            text = f"職業: 無\n{text}"
        return {
            "thumbnailImageUrl": counselor.image,
            "imageBackgroundColor": "#FFFFFF",
            "title": title,
            "text": text,
            "actions": [
                {
                    "type": "postback",
                    "label": "配對",
                    "text": f"我要配對 {counselor.user_name}",
                    "data" : f"action=pair&counselor_id={counselor.user_id}"
                },
            ]
        }

    target_type_condition = None
    for idx, target_type in enumerate(filter_types):
        if idx == 0:
            target_type_condition = Q(target=target_type)
        else:
            target_type_condition = target_type_condition | Q(target=target_type)
    counselors = models.Counselor.objects.filter(target_type_condition & Q(can_be_paired=True)).distinct()[0:10]
    if len(counselors) == 0:
        return {}
    return {
        "type": "template",
        "alt_text": "符合條件的諮商師",
        "template": {
            "type": "carousel",
            "columns": [generate_counselor_template(c) for c in counselors],
            "imageAspectRatio": "rectangle",
            "imageSize": "cover"
        }
    }

def send_counselors_information_to_user(user_id: str, filter_types: list):
    counselors_information = generate_counselors_information_template(filter_types)
    if counselors_information:
        send_to_user(user_id, TemplateSendMessage(**counselors_information))
    else:
        send_to_user(user_id, TextSendMessage(text="查不到相關的諮商師"))

def generate_patient_template(user_id, brief):
    user = line_bot_api.get_profile(user_id)
    return {
        "type": "template",
        "alt_text": "有人需要被諮商!",
        "template": {
            "type": "buttons",
            "thumbnailImageUrl": user.picture_url,
            "imageAspectRatio": "rectangle",
            "imageSize": "cover",
            "imageBackgroundColor": "#FFFFFF",
            "title": user.display_name,
            "text": f"{brief}",
            "actions": [
                {
                    "type": "postback",
                    "label": "接受",
                    "text" : "接受",
                    "data" : f"action=help&target_id={user_id}"
                },
            ]
        }
    }

def send_patient_information_to_counselor(counselor_id, user_id, brief):
    template = generate_patient_template(user_id, brief)
    send_to_user(counselor_id, TemplateSendMessage(**template))

