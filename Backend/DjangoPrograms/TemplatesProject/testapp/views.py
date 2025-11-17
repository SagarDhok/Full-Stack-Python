from django.shortcuts import render
import datetime
# Create your views here.
def display(request):
 date = datetime.datetime.now()
 name="karan"
 marks = "90"
 rollno = "10"
 my_dict = {"insert_date":date,"name":name,"marks":marks,"rollno":rollno}
 return render(request,template_name="testapp/wish.html",context=my_dict)