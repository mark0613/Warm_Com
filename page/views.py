from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def view_index_page(request):
    return render(request, 'index.html')

def view_pair_page(request):
    return render(request, 'pair.html')

def view_profile_page(request):
    return render(request, 'profile.html')