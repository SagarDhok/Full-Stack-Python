from django.shortcuts import render
from django.views import generic
from testapp.pagination import MyPagination, MyPagination2, MyPagination3
from rest_framework.generics import ListAPIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer

# Create your views here.





# class EmployeeListView(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    # pagination_class = MyPagination3



# class EmployeeListView(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
#     def get_queryset(self):
#         qs = Employee.objects.all()
#         name = self.request.GET.get('ename')
#         if name is not None:
#             qs = qs.filter(ename__contains=name)
#         return qs



class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # search_fields = ('ename',)
    # search_fields = ('eno',)
    # search_fields = ('^eno',)
    # search_fields = ('=eno',)
    ordering_fields = ('eno','esal')


