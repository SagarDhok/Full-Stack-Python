from django import forms

class Feedbackform(forms.Form):
                name= forms.CharField()
                rollno = forms.IntegerField()
                email = forms.EmailField()
                feedback = forms.CharField(widget=forms.Textarea)