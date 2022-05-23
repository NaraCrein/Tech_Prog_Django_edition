from django.urls import path
from .views import *
from . import views
from django.contrib import admin

urlpatterns = [
    path('', index, name='index'),
    path('detail/', Detail),
    path('admin/', admin.site.urls),
    path('add/', Add),
    path('forgot/', Forgot),
    path('reset/', Reset),
    path('profile/', Profile, name='profile'),
    path('signin/', LoginUser.as_view(), name='signin'),
    path('signup/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),

]
