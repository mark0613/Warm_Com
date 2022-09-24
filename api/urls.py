from django.urls import path
from . import views
 
urlpatterns = [
    path('pair', views.pair_porcess),
    path('appoint', views.appoint_process),
    path('counselor', views.counselor_profile_process),
    path('article', views.create_article),
    path('article/<int:id>', views.get_article),
    path('articles', views.get_articles),
    path('reply', views.create_reply),
]
