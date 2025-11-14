from django.shortcuts import render

# Create your views here.

from testapp.models import Employee
def retrieve_view(request):
    emp_list = Employee.objects.all()
    print(type(emp_list))
   # <class 'django.db.models.query.QuerySet'>
    return render(request,'testapp/index.html',{'emp_list':emp_list})