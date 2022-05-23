from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from Avito.models import Ad


class UserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=20)


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['name', 'price', 'image']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class': 'inp'}))
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'inp'}))
    password2 = forms.CharField(label='Повторите пароль',widget=forms.PasswordInput(attrs={'class': 'inp'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'inp'}),
            'password1': forms.PasswordInput(attrs={'class': 'inp'}),
            'password2': forms.PasswordInput(attrs={'class': 'inp'})

        }
