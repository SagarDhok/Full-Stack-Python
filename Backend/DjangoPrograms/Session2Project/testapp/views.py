from django.shortcuts import render
from testapp.forms import Loginform

# Create your views here.

def home_view(request):
                form = Loginform()
                return render(request, 'html/home.html',context={'form':form})

def datetime_view(request):
        name = request.GET.get('name')
        response = render(request,'html/datetime.html',context={'name':name})
        response.set_cookie('name',name)
        return response


def result_view(request):
        import datetime
        date = datetime.datetime.now()
        print(request.COOKIES)
        name = request.COOKIES.get('name')
        return render(request,'html/result.html',{'name':name,'date':date})
