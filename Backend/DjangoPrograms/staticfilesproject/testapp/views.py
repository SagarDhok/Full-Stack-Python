from django.shortcuts import render

# Create your views here.
def display(request):
                subject = {"s1":"python","s2":"java","s3":"datascience","s4":"devops"}
                return render(request,template_name="testapp/result.html",context=subject)