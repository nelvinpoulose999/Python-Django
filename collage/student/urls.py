"""collage URL Configuration

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
from .views import get_student_registeration,get_log,get_feed,fetch_data,fetch_login

urlpatterns = [
    path("studregister",get_student_registeration,name="studreg"),
    path("login",get_log,name="login"),
    path("feedback",get_feed,name="feedback"),
    path("fetchdata",fetch_data,name="fetchdata"),
    path("fetchlogin",fetch_login,name="fetchsignin")
]
