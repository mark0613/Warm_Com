from django.shortcuts import render
from django import http
from django.views.decorators.csrf import csrf_exempt

from chatbot.models import Counselor, Target, Article, Reply

from chatbot.views import (
    send_counselors_information_to_user,
    send_patient_information_to_counselor,
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
        # TODO: 發送好友ID給對方
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

@csrf_exempt
def counselor_profile_process(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_name = request.POST['user_name']
        gender = request.POST['gender']
        image = request.POST['image']
        age = get_null_value(request.POST['age'])
        job = get_null_value(request.POST['job'])
        description = request.POST['description']
        is_professional = bool(request.POST['is_professional'])
        can_be_paired = bool(request.POST['can_be_paired'])
        targets = request.POST.getlist('targets[]')
        counselor = Counselor.objects.create(
            user_id = user_id,
            user_name = user_name,
            gender = gender,
            image = image,
            age = age,
            job = job,
            description = description,
            is_professional = is_professional,
            can_be_paired = can_be_paired,
        )
        for target in targets:
            counselor.target.add(Target.objects.get(id=target))
        return http.JsonResponse({ "message" : "成功" }, status=201)

@csrf_exempt
def create_article(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(user_id, title, content)
        article = Article.objects.create(creator=user_id, title=title, content=content)
        article.save()
        return http.JsonResponse({'message': '成功'}, status=201)
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
            'time': reply.time
        })
    return_data['replies'] = reply_data
    return_data['time'] = article.time
    return http.JsonResponse(return_data, status=201)

@csrf_exempt
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