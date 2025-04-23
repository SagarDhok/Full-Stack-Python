from django import forms

class StudentForm(forms.Form):
  Name = forms.CharField() #no need to specify max-lenght
  Marks = forms.IntegerField()