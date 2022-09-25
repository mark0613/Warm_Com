from django.shortcuts import render
from django import http
from django.views.decorators.csrf import csrf_exempt

from chatbot.models import Counselor, Target, Article, Reply

from chatbot.views import (
    send_counselors_information_to_user,
    send_patient_information_to_counselor,
    send_message,
)

import random

pair_brief_table = {}

@csrf_exempt
def pair_porcess(request):
    global pair_brief_table
    if request.method == 'POST':
        user_id = request.POST['user_id']
        brief = request.POST['brief']
        types = request.POST.getlist('types[]')
        pair_brief_table[user_id] = {
            "brief" : brief,
            "types" : types,
        }
        send_counselors_information_to_user(user_id, types)
        return http.JsonResponse(
            {
                "message" : "成功",
            },
            status=201
        )

@csrf_exempt
def appoint_process(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        counselor_id = request.POST['counselor_id']
        send_patient_information_to_counselor(counselor_id, user_id, pair_brief_table[user_id]["brief"])
        return http.JsonResponse(
            {
                "message" : "成功",
            },
            status=201
        )

@csrf_exempt
def help_process(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        counselor_id = request.POST['counselor_id']
        counselor_line_id = Counselor.objects.filter(user_id=counselor_id).first().line_id
        send_message(user_id, f"諮商師已接受，這是他的 line id:\n{counselor_line_id}\n或是點選連結快速開啟:\nhttps://line.me/ti/p/~{counselor_line_id}")
        return http.JsonResponse(
            {
                "message" : "成功",
            },
            status=201
        )

def get_null_value(value):
    if value == '':
        return None
    return value

def get_formatting_date(date):
    return date.strftime('%Y-%m-%d %H:%M:%S')

@csrf_exempt
def counselor_profile_process(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_name = request.POST['user_name']
        line_id = request.POST['line_id']
        gender = request.POST['gender']
        image = request.POST['image']
        age = get_null_value(request.POST['age'])
        job = get_null_value(request.POST['job'])
        description = request.POST['description']
        is_professional = bool(request.POST['is_professional'])
        can_be_paired = bool(request.POST['can_be_paired'])
        targets = request.POST.getlist('targets[]')
        user_exist = Counselor.objects.filter(user_id=user_id).count() > 0
        if user_exist:
            counselor = Counselor.objects.get(user_id=user_id)
            counselor.user_name = user_name
            counselor.line_id = line_id
            counselor.gender = gender
            counselor.image = image
            counselor.age = age
            counselor.job = job
            counselor.description = description
            counselor.is_professional = is_professional
            counselor.can_be_paired = can_be_paired
            counselor.target.set(targets)
            counselor.save()
        else:
            Counselor.objects.create(
                user_id = user_id,
                user_name = user_name,
                line_id = line_id,
                gender = gender,
                image = image,
                age = age,
                job = job,
                description = description,
                is_professional = is_professional,
                can_be_paired = can_be_paired,
            ).target.set(targets)
        return http.JsonResponse({ "message" : "成功" }, status=201)

def get_counselor_profile(request, user_id):
    try:
        counselor = Counselor.objects.get(user_id=user_id)
    except Counselor.DoesNotExist:
        return http.JsonResponse({'message': '失敗'}, status=404)
    result = {}
    result["user_id"] = counselor.user_id
    result["user_name"] = counselor.user_name
    result["line_id"] = counselor.line_id
    result["gender"] = counselor.gender
    result["image"] = counselor.image
    result["age"] = counselor.age
    result["job"] = counselor.job
    result["description"] = counselor.description
    result["is_professional"] = counselor.is_professional
    result["can_be_paired"] = counselor.can_be_paired
    result["targets"] = [target.id for target in counselor.target.all()]
    return http.JsonResponse(result, status=200)


@csrf_exempt
def create_article(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.create(creator=user_id, title=title, content=content)
        article.save()
        result = {
            'message' : '成功',
            'article_id' : article.id,
        }
        return http.JsonResponse(result, status=201)
    return http.JsonResponse({'message': '失敗'}, status=404)

def get_article(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return http.JsonResponse({'message': '失敗'}, status=404)
    return_data = {}
    return_data['title'] = article.title
    return_data['content'] = article.content

    replies = Reply.objects.filter(article=article)
    reply_data = []
    for reply in replies:
        reply_data.append({
            'reply_id': reply.id,
            'content': reply.content,
            'time': get_formatting_date(reply.time),
        })
    return_data['replies'] = reply_data
    return_data['time'] = get_formatting_date(article.time)
    return http.JsonResponse(return_data, status=201)

def get_articles(request):
    limit = int(request.GET.get('limit'))
    articles = random.sample(list(Article.objects.all()), limit)
    result = []
    for article in articles:
        a_id = article.id
        replies = Reply.objects.filter(article=a_id).count()
        result.append({
            "article_id" : a_id,
            "replies" : replies,
        })
    return http.JsonResponse(result, status=200, safe=False)

def get_user_articles(request, user_id):
    articles = Article.objects.filter(creator=user_id).order_by('-time')
    result = []
    for article in articles:
        result.append({
            "article_id" : article.id,
            "title" : article.title,
            "content" : article.content,
            "time" : get_formatting_date(article.time),
            "replies" : Reply.objects.filter(article=article.id).count(),
        })
    return http.JsonResponse({ "articles" : result }, status=200)

@csrf_exempt
def create_reply(request):
    if request.method == 'POST':
        article_id = request.POST.get('article_id')
        user_id = request.POST.get('user_id')
        content = request.POST.get('content')
        article = Article.objects.get(id=article_id)
        reply = Reply.objects.create(article=article, creator=user_id, content=content)
        reply.save()
        return http.JsonResponse({'message': '成功'}, status=201)
    return http.JsonResponse({'message': '失敗'}, status=404)