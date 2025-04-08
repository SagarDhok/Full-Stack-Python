from django.shortcuts import render
import datetime

# Create your views here.
def info_view(request):
  time = datetime.datetime.now()
  Name = "Django"
  Prerequisite="Python"
  mydict  = {"Name":Name,"Prerequisite":Prerequisite,"Time":time}
  return render(request,template_name="testapp\\result.html",context=mydict)

  