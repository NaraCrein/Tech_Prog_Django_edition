from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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


class AddAdForm(forms.ModelForm):
    name = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'inp'}))
    price = forms.IntegerField(label='Цена', widget=forms.NumberInput(attrs={'class': 'inp'}))
    place = forms.CharField(label='Местонахождение', widget=forms.TextInput(attrs={'class': 'inp'}))
    desc = forms.CharField(label='Описание', widget=forms.TextInput(attrs={'class': 'inp'}))
    image = forms.ImageField(label='Фото', widget=forms.FileInput(attrs={'class': 'inp'}))
    seller = forms.CharField(label='Имя продавца', widget=forms.TextInput(attrs={'class': 'inp'}))
    phone = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'inp'}))

    class Meta:
        model = Ad
        fields = ('name', 'price', 'place', 'desc', 'image', 'seller', 'phone')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'inp'}),
            'price': forms.NumberInput(attrs={'class': 'inp'}),
            'place': forms.TextInput(attrs={'class': 'inp'}),
            'desc': forms.TextInput(attrs={'class': 'inp'}),
            'image': forms.FileInput(attrs={'class': 'inp'}),
            'seller': forms.TextInput(attrs={'class': 'inp'}),
            'phone': forms.TextInput(attrs={'class': 'inp'})
        }
