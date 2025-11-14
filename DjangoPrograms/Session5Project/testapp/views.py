from django.shortcuts import render
from testapp.forms import NameForm,AgeForm,GfForm

# Create your views here.

def Name_view(request):
                form = NameForm()
                return render(request,'html/name.html',{'form':form})

def Age_view(request):
             form = AgeForm()
             name = request.GET["name"]
             request.session['name']= name
             return  render(request,"html/age.html",{"form":form,'name':name})

def Gf_view(request):
        form = GfForm()
        name = request.session["name"]
        age = request.GET["age"]
        age = request.session["age"]=age
        return  render(request,"html/gf.html",{"form":form,'name':name})


def Result_view(request):
        name = request.session["name"]
        age = request.session["age"]
        gf = request.GET["gf"]
        request.session['gf'] = gf
        return  render(request,"html/result.html",{'name':name,"age":age,"gf":gf})
