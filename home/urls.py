from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.home, name='home'),
    path('send_mail', views.send_mail_func, name='send_mail_func'),
    path('page_2', views.page_two, name='page_two'),          
]