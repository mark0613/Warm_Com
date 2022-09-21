from django import http
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
 
from linebot import LineBotApi, WebhookParser
from linebot.models import TextSendMessage


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def receive_message(request):
    return http.HttpResponse()

def send_to_user(user_id: str, message: str):
    line_bot_api.push_message(user_id, TextSendMessage(text=message))
