"""mycollage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import get_registeration,fetch_register,get_login,fetch_login

urlpatterns = [
    path('facuregister',get_registeration),
    path('fetchfacregister',fetch_register,name='fetchfacregister'),
    path('faculogin',get_login),
    path('fetchfaclogin',fetch_login,name='fetchfaclogin')

]
