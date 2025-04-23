from django.shortcuts import render
from testapp.forms import Feedbackform

# Create your views here.

def feedback_view(request):
                submitted = False
                name = ''

                if request.method == "POST":
                        form = Feedbackform(request.POST)
                        if form.is_valid():
                                  print('Form validation success and printing feedback information')
                                  print('*'*55)
                                  print('Name:',form.cleaned_data['name'])
                                  print('RollNo:',form.cleaned_data['rollno'])
                                  print('Mail ID:',form.cleaned_data['email'])
                                  print('Feedback:',form.cleaned_data['feedback'])
                                  submitted = True
                                  name = form.cleaned_data['name']
                form = Feedbackform()
                return render(request,'html/index.html', {'form':form, 'submitted':submitted,'name':name})