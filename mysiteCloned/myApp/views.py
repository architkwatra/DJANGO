from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello to my first django app')

def helloWorld(request):
    return HttpResponse('Hello World') 