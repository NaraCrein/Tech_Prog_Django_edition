from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Avito.models import Ad
from .forms import RegisterUserForm

from .models import Ad
from .utils import DataMixin


def Detail(request):
    return render(request, 'Detail/detail.html')


def index(request):
    Ad_list = Ad.objects.all()
    template = loader.get_template('Main/main.html')
    context = {
        'Ad_list': Ad_list
    }
    return HttpResponse(template.render(context, request))


def SignIn(request):
    return render(request, 'Sign/SignIn.html')


def Add(request):
    return render(request, 'Add/add.html')


def Forgot(request):
    return render(request, 'Forgot/Forgot.html')


def Reset(request):
    return render(request, 'Forgot/Reset.html')


def Profile(request):
    return render(request, 'Profile/Profile.html')


def SignUp(request):
    return render(request, 'Sign/SignUp.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "Sign/SignUp.html"
    success_url = reverse_lazy('signin')
1