from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from chatbot.models import Article


@csrf_exempt
def view_index_page(request):
    return render(request, 'index.html')

def view_pair_page(request):
    return render(request, 'pair.html')

def view_profile_page(request):
    return render(request, 'profile.html')

def view_give_all_page(request):
    return render(request, 'give_all.html')

def view_give_page(request, id):
    article = Article.objects.get(id=id)
    content = {
        "article" : article
    }
    return render(request, 'give.html', content)

def view_receive_all_page(request):
    return render(request, 'receive_all.html')

def view_receive_page(request):
    return render(request, 'receive.html')

def view_article_page(request):
    return render(request, 'article.html')