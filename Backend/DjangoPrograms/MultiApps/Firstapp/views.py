from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def display1(request):
     msg = "<h1>THis is First APp</h1>"
     return HttpResponse(msg)