from django.shortcuts import render
from testapp.forms import StudentForm

# Create your views here.

def student_input_view(request):
                form = StudentForm()
                mydict = {"form":form}
                return render (request,"html/index.html",context=mydict)