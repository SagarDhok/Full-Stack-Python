from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def Firstview(request):
     msg = "<h1>This is First View</h1>"
     return HttpResponse(msg)