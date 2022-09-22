from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.view_index_page),
    path('pair', views.view_pair_page),
    path('profile', views.view_profile_page)
]
