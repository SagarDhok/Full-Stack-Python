from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def home_view(request):
                return render(request, 'html/home.html')

@login_required
def java_page_view(request):
    return render(request,'html/javaexams.html')
#* Page not found (404)
#* Request Method:	GET
#* Request URL:	http://127.0.0.1:8000/accounts/login/?next=/java/
#* Solved this problem by including auth application url's


def python_page_view(request):
    return render(request,'html/pythonexams.html')

def aptitude_page_view(request):
    return render(request,'html/aptitudeexams.html')

def logout_view(request):
    return render(request,'html/logout.html')


from testapp.forms import Signupform
def Signup_view(request):
      form = Signupform()
      if request.method=="POST":
            form = Signupform(request.POST)
            user = form.save()  #form madhe field ahe password
            user.set_password(user.password)#set password funtion ahe
            
            user.save()
            return HttpResponseRedirect("/accounts/login")
      return render(request,'html/signup.html',{'form':form})

