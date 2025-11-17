from django.shortcuts import render
from Jobsapp.models import Hydjobs,Punejobs,Bangjobs

# Create your views here.

def home_page_view(request):
                return render(request, "testapp/index.html")        

def hydjobs_info(request):
        hydjobs_list =  Hydjobs.objects.all()
        dict = {"hydjobs_list":hydjobs_list,"type":"hyd"}
        return render(request,"testapp/jobs.html",context = dict)

def punejobs_info(request):
        punejobs_list =  Punejobs.objects.all()
        dict = {"punejobs_list":punejobs_list,"type":"pune"}
        return render(request,"testapp/jobs.html",context=dict)

def banglorejobs_info(request):
        bngjobs_list =  Bangjobs.objects.all()
        dict = {"bngjobs_list":bngjobs_list,"type":"bang"}
        return render(request,"testapp/jobs.html",context=dict)