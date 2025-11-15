from django.shortcuts import render
from django.db.models import Q

# Create your views here.

from testapp.models import Employee
def retrieve_view(request):
    # emp_list = Employee.objects.all()
    # emp_list = Employee.objects.get(id__exact=51)
    # emp_list = [Employee.objects.get(id=51)] #!1. get() → single object Not iterable  → loop nahi chalega
    #!loop chalvayha asel tr list madhe
    # emp_list = Employee.objects.filter(esal__gte = 15000)
    # emp_list = Employee.objects.filter(esal__lt=11000)
    # emp_list = Employee.objects.filter(ename__contains = 'su')
    # emp_list = Employee.objects.filter(eno__contains = '1')
    # emp_list = Employee.objects.filter(id__in = [51,1,5])
    # emp_list = Employee.objects.filter(ename__startswith="A")
    # emp_list = Employee.objects.filter(ename__endswith="r")
    # emp_list = Employee.objects.filter(esal__range=[10000,15000])
    # emp_list = Employee.objects.filter(ename__startswith="S")| Employee.objects.filter(esal__lt = 10001)
    # emp_list = Employee.objects.filter(Q(ename__startswith="A")|Q(esal__lt = 10001))
    # emp_list = Employee.objects.filter(ename__startswith="S")& Employee.objects.filter(esal__lt = 15000)
    # emp_list = Employee.objects.filter(Q(ename__startswith="S")& Q(esal__lt = 18000))
    # emp_list = Employee.objects.filter(ename__startswith="S",esal__lt = 15000)
    # emp_list = Employee.objects.exclude(ename__startswith="m")
    # emp_list = Employee.objects.exclude()
    # emp_list = Employee.objects.filter(~Q(ename__startswith = "s"))
    # emp_list = Employee.objects.filter(~Q(esal__gte=15000))
    # emp_list = Employee.objects.all().values_list("ename",'esal')
    # emp_list = Employee.objects.all().values("ename",'esal')
    emp_list = Employee.objects.all().only("ename",'esal')
    return render(request,'testapp/specificcolumns.html',{'emp_list':emp_list})


    



    # print(type(emp_list))
    # return render(request,'testapp/index.html',{'emp_list':emp_list})