# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .tasks import sendemail
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import requests

# Create your views here.

def send_email(request):
    sendemail.delay()
    return HttpResponse('<h1>send email</h1>')

@cache_page(60)
def test(request):
    response = requests.get("https://432aec5b-2450-46fc-ac4f-cb32378717d6.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())