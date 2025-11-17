from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hyd_jobs_info(request):
     s = "<h1>Hydrabad jobs information</h1>"
     return HttpResponse(s)

def bang_jobs_info(request):
     s = "<h1>Banglore jobs information</h1>"
     return HttpResponse(s)

def pune_jobs_info(request):
     s = "<h1>Pune jobs information</h1>"
     return HttpResponse(s)


def bihar_jobs_info(request):
     s = "<h1>Bihar jobs information</h1>"
     return HttpResponse(s)