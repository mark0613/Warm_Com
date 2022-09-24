from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.view_index_page),
    path('pair', views.view_pair_page),
    path('profile', views.view_profile_page),
    path('candles', views.view_candles_page),
    path('reply/<int:id>', views.view_reply_page),
    path('my-articles', views.view_my_articles_page),
    path('receive', views.view_receive_page),
    path('article', views.view_article_page)
]
