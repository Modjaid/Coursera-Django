from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    text = "<h1> Welcome to Little Lemon! </h1> "
    return HttpResponse(text)
