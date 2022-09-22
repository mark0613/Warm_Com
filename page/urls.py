from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.view_index_page),
    path('pair', views.view_pair_page),
    path('profile', views.view_profile_page),
    path('give_all', views.view_give_all_page),
    path('give', views.view_give_page)
]
