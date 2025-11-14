from django.shortcuts import render

# Create your views here.


def home_view(request):
                return render(request,'html/home.html')


def age_view(request):
        print(request.COOKIES)
        name = request.GET['name']
        response = render(request,'html/age.html',{'name':name})
        response.set_cookie('name',name)
        return response

def gf_view(request):
        print(request.COOKIES)
        name = request.COOKIES.get('name')
        age = request.GET['age']
        response = render(request,'html/gf.html',{'name':name})
        response.set_cookie('age',age)
        return response

def result_View(request):
        print(request.COOKIES)
        name = request.COOKIES.get('name')
        age = request.COOKIES.get('age')
        gf = request.GET['gf']
        return render(request,'html/result.html',{'name':name,'age':age,'gf':gf})


        