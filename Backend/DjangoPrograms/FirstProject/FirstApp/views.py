from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display(request):   #can take any argument but should take only requist for convinienve 
     s = "<h1> MY Name Is Anthony Gunjalwish </h1>"
     return HttpResponse(s)    #object crated
