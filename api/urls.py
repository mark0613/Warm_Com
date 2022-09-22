from django.urls import path
from . import views
 
urlpatterns = [
    path('pair', views.pair_porcess),
    path('appoint', views.appoint_process),
]
