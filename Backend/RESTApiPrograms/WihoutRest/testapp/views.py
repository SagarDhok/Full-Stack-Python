from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def emp_data_view(request):
                emp_data = {
                                'eno':101,
                                'ename':'Sunny',
                                'esal':12000,
                                 'eaddr':'Mumbai'
                }

                resp = f"""<h1>
                Employee Number : {emp_data['eno']}<br>
                Employee Name : {emp_data['ename']}<br>
                Employee Salary : {emp_data['esal']}<br>
                Employee Adress : {emp_data['eaddr']}<br>
                </h1>"""

                return HttpResponse(resp)
