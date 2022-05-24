from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, _unicode_ci_compare
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.forms import ModelForm
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


from Avito.models import Ad, TUser


class UserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=20)


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['name', 'price', 'image']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'inp'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'inp'}))
    first_name = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'inp'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'inp'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'inp'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'inp'}),
            'email': forms.EmailInput(attrs={'class': 'inp'}),
            'first_name': forms.TextInput(attrs={'class': 'inp'}),
            'password1': forms.PasswordInput(attrs={'class': 'inp'}),
            'password2': forms.PasswordInput(attrs={'class': 'inp'})

        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'inp'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'inp'}))


