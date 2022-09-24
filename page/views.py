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

def view_candles_page(request):
    return render(request, 'candles.html')

def view_reply_page(request, id):
    article = Article.objects.get(id=id)
    content = {
        "article" : article
    }
    return render(request, 'reply.html', content)

def view_my_articles_page(request):
    return render(request, 'my_articles.html')

def view_receive_page(request):
    return render(request, 'receive.html')

def view_article_page(request):
    return render(request, 'article.html')