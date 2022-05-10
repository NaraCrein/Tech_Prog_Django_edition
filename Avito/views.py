from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Avito.models import Ad

from .models import Ad


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








