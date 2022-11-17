# from django.shortcuts import render
from django.http import HttpResponse
from time import sleep
from .tasks import sendemail

# Create your views here.

def send_email(request):
    sendemail.delay()
    return HttpResponse('<h1>send email</h1>')
