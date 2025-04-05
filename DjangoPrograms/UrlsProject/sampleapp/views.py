from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(request):
     msg = "<h1>This is first View </h1>"
     return HttpResponse(msg)


def second_view(request):
     msg = "<h1>This is Second View </h1>"
     return HttpResponse(msg)

def third_view(request):
     msg = "<h1>This is third View </h1>"
     return HttpResponse(msg)