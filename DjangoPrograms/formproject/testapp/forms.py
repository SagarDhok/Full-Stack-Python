from django import forms

class StudentForm(forms.Form):
  name = forms.CharField() #no need to specify max-lenght
  marks = forms.IntegerField()