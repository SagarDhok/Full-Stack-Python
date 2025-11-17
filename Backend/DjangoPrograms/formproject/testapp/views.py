from django.shortcuts import render
from testapp.forms import StudentForm

# Create your views here.

def student_input_view(request):
                submitted = False
                sname = " "
                
                if request.method == "POST":
                        form = StudentForm(request.POST)
                        if form.is_valid():
                         print("FOrm Validaiton is Succesfull and print data")
                         print("Rollno : ",form.cleaned_data["Rollno"])
                         print("Name : ",form.cleaned_data["Name"])
                         print("Marks :",form.cleaned_data["Marks"])
                         submitted = True
                         sname = form.cleaned_data["Name"]
              
                form = StudentForm()
                return render (request,"html/index.html",context={"form":form,"submitted":submitted,"sname":sname})