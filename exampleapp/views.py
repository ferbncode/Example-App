from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.kk

def index(request):
    return HttpResponse("Hello, I am here and I am writing nothing")
