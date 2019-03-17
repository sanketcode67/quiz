from django.urls import path
from django.contrib.auth import views
from . import views
from accounts.forms import LoginForm


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    ]
