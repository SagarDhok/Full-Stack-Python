from django import forms
from testapp.models import movies

class MovieForm(forms.ModelForm):
                rdate = forms.DateField(
                  widget=forms.DateInput(attrs={'type': 'date'})  # Shows HTML5 calendar input 🗓️
           )

                class Meta:
                        model = movies
                        fields = "__all__"
