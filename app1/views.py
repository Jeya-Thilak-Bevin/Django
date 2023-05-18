from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    message = '<h1> Hi Buddy how are you </h1>'
    return HttpResponse(message)
