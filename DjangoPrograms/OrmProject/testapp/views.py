from django.shortcuts import render
from django.db.models import Q

# Create your views here.

from testapp.models import Employee
from django.db.models.functions import Lower
def retrieve_view(request):
    emp_list = Employee.objects.all()
    # e = Employee(eno=1234,ename='Lilly',esal=12000,eaddr='Chennai')
    # Employee.objects.create(eno=0000,ename='sssss',esal=14000,eaddr='Delhi')
    # Employee.objects.bulk_create([
    #     Employee(eno=101, ename='Amit',    esal=25000, eaddr='Delhi'),
    #     Employee(eno=202, ename='Riya',    esal=30000, eaddr='Pune'),
    #     Employee(eno=303, ename='Vikram',  esal=28000, eaddr='Hyderabad'),
    # ])
    # e = Employee.objects.get(eno=101)
    # e.delete()
    # qs = Employee.objects.filter(esal__gte=15000)
    # qs.delete()
    # Employee.objects.all().delete()
    # e = Employee.objects.get(id=164)
    # e.ename='Sunny'
    # e.esal = 18000
    # e.eaddr = 'Mumbai'
    # e.save()
    # emp_list = Employee.objects.all().order_by('eno')
    # emp_list = Employee.objects.all().order_by('-eno')
    # emp_list = Employee.objects.all().order_by('ename')
    # emp_list = Employee.objects.all().order_by(Lower('ename'))
    q1 = Employee.objects.filter(esal__lt=12000)
    q2 = Employee.objects.filter(ename__startswith='s')
    emp_list = q1.union(q2)

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
    # emp_list = Employee.objects.all().only("ename",'esal')
    # return render(request,'testapp/specificcolumns.html',{'emp_list':emp_list})
    # print(type(emp_list))
    return render(request,'testapp/index.html',{'emp_list':emp_list})

from django.db.models import Avg,Max,Min,Sum,Count
def aggregate_view(request):
        avg = Employee.objects.all().aggregate(Avg('esal'))
        max = Employee.objects.all().aggregate(Max('esal'))

        mydict = {'avg':avg["esal__avg"],'max':max['esal__max']}
        
        min = Employee.objects.all().aggregate(Min('esal'))
        sum = Employee.objects.all().aggregate(Sum('esal'))
        count = Employee.objects.all().aggregate(Count('esal'))
        my_dict = {'avg':avg['esal__avg'], 'max':max['esal__max'], 'min':min['esal__min'], 'sum':sum['esal__sum'],'count':count['esal__count']}
        return render(request,'testapp/aggregate.html',context= mydict)