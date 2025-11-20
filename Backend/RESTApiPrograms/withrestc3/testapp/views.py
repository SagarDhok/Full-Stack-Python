from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.response import Response

# class EmployeeListAPIView(APIView):
#     def get(self,request):
#         qs = Employee.objects.all()
#         serializer = EmployeeSerializer(qs,many=True)
#         return Response(serializer.data)

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView,DestroyAPIView
# class EmployeeListAPIView(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class EmployeeCreateAPIView(CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer



# class EmployeeRetrieveView(RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field="id"


# class EmployeeUpdateAPIView(UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'id'

class EmployeeDestroyAPIView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'