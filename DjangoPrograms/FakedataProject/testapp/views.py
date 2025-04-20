from django.shortcuts import render
from testapp.models import Student

# Create your views here.

def student_view(request):
                # student_list = Student.objects.all()
                # student_list = Student.objects.filter(marks__gte=98) #>=98
                # student_list = Student.objects.filter(name__startswith = "S")
                # student_list = Student.objects.all().order_by("marks")  #ascending order
                student_list = Student.objects.all().order_by("-marks") #descending order
                mydict = {"student_list":student_list}
                return render(request,template_name="testapp\std.html",context=mydict)