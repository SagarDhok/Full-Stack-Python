from django import forms


class Additemform(forms.Form):
                itemname = forms.CharField()
                quantity = forms.IntegerField()
    