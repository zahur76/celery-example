"""
    All imports
"""
from os import stat_result
from django.core.mail import send_mail
from django.http import response
from django.shortcuts import (
    render, reverse, redirect, get_object_or_404, HttpResponse)
import time
from celery_example.celery import app
from .tasks import sleepy, send_email_task, long_task
from django.core.mail import send_mail


def home(request):
    """ A view to return the home page with site request"""   
    sleepy.delay(10)
    return render(request, 'home/index.html')

def page_two(request):
    """ A view to return the second page with site request"""   
    
    return render(request, 'home/second.html')

def send_mail_func(request):
    long_task()
    return render(request, 'home/index.html')