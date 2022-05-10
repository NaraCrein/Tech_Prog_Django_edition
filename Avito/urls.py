from django.urls import path
from .views import *
from . import views
from django.contrib import admin

urlpatterns = [
    path('', index, name='index'),
    path('detail/', Detail),
    path('admin/', admin.site.urls),
    path('add/', SignIn),
    path('forgot/', Forgot),
    path('reset/', Reset),
    path('profile/', Profile),
    path('signin/', SignIn),
    path('signup/', SignUp),

]