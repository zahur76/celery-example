from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def sleepy(duration):
    sleepy(duration)
    
    return None


@shared_task
def send_email_task():
    for x in range(0,4):
        send_mail('celery task worked!',
        'This worked!',
        'support@hotmail.com',
        ['zahurmeerun@hotmail.com'])   
    return None


@shared_task
def long_task():
    zahur  = []
    for x in range (0,10):
        zahur.append(x)
        sleep(1)
    print(zahur)
    return None