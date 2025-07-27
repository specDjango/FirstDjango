from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello Maxim. THis is sample Django app response")


def news(request):
    return HttpResponse("News")


