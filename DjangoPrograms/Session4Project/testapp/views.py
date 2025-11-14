from django.shortcuts import render
from testapp.forms import Additemform

# Create your views here.


def home_view(request):
                return render(request,'html/home.html')


def additem_view(request):
        form = Additemform()
        response =  render(request,'html/additem.html',context={'form':form}) 
        if request.method =="POST":
                form = Additemform(request.POST)
                if form.is_valid():
                        name = form.cleaned_data["itemname"]
                        quantity = form.cleaned_data["quantity"]
                response.set_cookie(name,quantity)
        return response

def viewitem_view(request):
        return render(request,'html/viewitem.html')