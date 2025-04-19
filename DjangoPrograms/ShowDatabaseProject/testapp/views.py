from django.shortcuts import render
from testapp.models import Employee

# Create your views here.


def show_database(request):
   emp_list  =Employee.objects.all() #select * from employee
   my_dict = {"emp_list":emp_list}
   return render(request,template_name="testapp/emp.html",context=my_dict)