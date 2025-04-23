from django import forms

class student(forms.Form):
  name = forms.CharField() #no need to specify max-lenght
  marks = forms.IntegerField()