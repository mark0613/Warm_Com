from django.shortcuts import render
from django import http
from django.views.decorators.csrf import csrf_exempt

from chatbot.models import Counselor, Target

from chatbot.views import (
    send_counselors_information_to_user,
    send_patient_information_to_counselor,
)


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