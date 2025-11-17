from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def Thirdview(request):
     msg = "<h1>This is Third View</h1>"
     return HttpResponse(msg)