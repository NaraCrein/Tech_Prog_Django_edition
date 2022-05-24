from django.urls import path
from .views import *
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('detail/', Detail),
    path('admin/', admin.site.urls),
    path('add/', AddAd.as_view(), name='add'),
    path('forgot/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/', Reset),
    path('profile/', Profile, name='profile'),
    path('signin/', LoginUser.as_view(), name='signin'),
    path('signup/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
