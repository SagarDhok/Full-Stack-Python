from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display2(request):
     msg = "<h2>This is Second App</h2>"
     return HttpResponse(msg)