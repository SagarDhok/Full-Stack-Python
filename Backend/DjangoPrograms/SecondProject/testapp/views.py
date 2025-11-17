from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def time_info(request):
     date = datetime.datetime.now()
     h = int(date.strftime("%H"))
     msg = "<h1> hello Guest very "
     if h<12:
          msg += "Good Morning"
     elif h<16:
          msg += "Good Afternoon"
     elif h<21:
          msg += "Good Evening"
     else:
          msg += "Good Night"

     msg +=  "</h1><hr>"
     msg += "<h1>Now The Sever Time is :"+str(date)+"</h1>"
     return HttpResponse(msg)




      

     return HttpResponse(msg)

