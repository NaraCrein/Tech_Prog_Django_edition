from django import forms
from django.forms import ModelForm

from Avito.models import Ad


class UserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=20)


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['name', 'price', 'image']