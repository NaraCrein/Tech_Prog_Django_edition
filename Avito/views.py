from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from Avito.models import Ad
from .forms import RegisterUserForm, LoginUserForm, AddAdForm

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
    if request.method == 'POST':
        form = AddAdForm(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddAdForm()
    return render(request, 'Add/add.html')


def Forgot(request):
    return render(request, 'Forgot/Forgot.html')


def Reset(request):
    return render(request, 'Forgot/Reset.html')


def Profile(request):
    return render(request, 'Profile/Profile.html')


def SignUp(request):
    return render(request, 'Sign/SignUp.html')

class SearchResultsView(ListView):
    model = Ad
    template_name = 'Search/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '')

        if query:
            object_list = Ad.objects.filter(
                Q(name__icontains=query) | Q(price__icontains=query)
            )
        else:
            object_list = Ad.objects.all()
        return object_list

class DetailView(ListView):
    model = Ad
    template_name = 'Detail/detail.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '')

        if query:
            object_ad = Ad.objects.filter(id__icontains=query)
        else:
            object_ad = Ad.objects.all()
        return object_ad


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "Sign/SignUp.html"
    success_url = reverse_lazy('signin')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'Sign/SignIn.html'

    def get_success_url(self):
        return reverse_lazy('profile')


def logout_user(request):
    logout(request)
    return redirect('signin')


class AddAd(CreateView):
    form_class = AddAdForm
    template_name = "Add/add.html"
    success_url = reverse_lazy('add')
