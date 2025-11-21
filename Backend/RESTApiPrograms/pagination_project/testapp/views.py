from django.shortcuts import render
from django.views import generic

# Create your views here.



from testapp.pagination import MyPagination, MyPagination2, MyPagination3
from rest_framework.generics import ListAPIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = MyPagination3



