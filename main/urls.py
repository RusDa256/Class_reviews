from urllib import request
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('all_fbs', views.all_fb, name = 'all')
]
