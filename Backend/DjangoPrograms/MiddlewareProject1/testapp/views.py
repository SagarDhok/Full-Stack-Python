from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def welcome_view(request):
    print('This line added by view function')
    return HttpResponse('<h1>Custom Middleware Demo</h1>')
