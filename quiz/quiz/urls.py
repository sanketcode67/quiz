from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from django.views.generic.base import TemplateView
from question.views import question_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',question_details,name='home'),
]
