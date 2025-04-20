from django.shortcuts import render
from testapp.models import Student

# Create your views here.

def student_view(request):
                student_list = Student.objects.all()
                mydict = {"student_list":student_list}
                return render(request,template_name="testapp\std.html",context=mydict)