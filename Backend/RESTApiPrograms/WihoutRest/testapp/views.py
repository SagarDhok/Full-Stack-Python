from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json

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


def emp_data_json_view(request):
    emp_data = {
        'eno':102,
        'ename':'Radhika',
        'esal':15000,
        'eaddr':'Vja'
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data,content_type = 'application/json')


def emp_data_json_view2(request):
    emp_data = {
        'eno':103,
        'ename':'Lilly',
        'esal':18000,
        'eaddr':'Bng'
    }
    return JsonResponse(emp_data)


from django.views.generic import View
# class JSONCBV(View):
    # def get(self,request,*args,**kwargs):
    #     emp_data = {
    #         'eno':101,
    #         'ename':'Katrina',
    #         'esal':22000,
    #         'eaddr':'Mumbai'
    #     }
    #     return JsonResponse(emp_data)
    
    # def get(self,request,*args,**kwargs):
    #     json_data = json.dumps({'msg':'This is from GET Method'})
    #     return HttpResponse(json_data,content_type='application/json')

    # def delete(self,request,*args,**kwargs):
    #     json_data = json.dumps({'msg':'This is from DELETE Method'})
    #     return HttpResponse(json_data,content_type='application/json')


    # def put(self,request,*args,**kwargs):
    #     json_data = json.dumps({'msg':'This is from PUT Method'})
    #     return HttpResponse(json_data,content_type='application/json')
    

    
    # def post(self,request,*args,**kwargs):
    #     json_data = json.dumps({'msg':'This is from POST Method'})
    #     return HttpResponse(json_data,content_type='application/json')
   

from testapp.mixins import HttpResponseMixin
class JSONCBV(HttpResponseMixin,View):
     def get(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':'This is from GET Method'})
        return self.rende_to_http_response(json_data)