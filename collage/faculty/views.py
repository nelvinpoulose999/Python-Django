from django.shortcuts import render,redirect
from .form import FacultyRegisterationform,FacultyLoginForm

# Create your views here.

# Registeration
def get_register(request):
    form=FacultyRegisterationform()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=FacultyRegisterationform(request.POST)
        if form.is_valid():
            Username=form.cleaned_data.get("Username")
            Lastname=form.cleaned_data.get("Lastname")
            Password=form.cleaned_data.get("Password")
            Phone=form.cleaned_data.get("PhoneNumber")
            Course=form.cleaned_data.get("Course")
            Age=form.cleaned_data.get("Age")
            print(Username,Lastname,Password,Phone,Course,Age)
            return redirect("login")
        else:
            form = FacultyRegisterationform(request.POST)
            context["form"]=form
            return render(request, "faculty/registeration.html", context)

    return render(request,"faculty/registeration.html",context)

def fetch_data(request):
    username=request.POST.get("uname")
    lastname=request.POST.get("lname")
    password=request.POST.get("pwd")
    print(username,lastname,password)
    return render(request, "faculty/login.html")

# Login
def get_login(request):
    form=FacultyLoginForm()
    context={}
    context["form"]=form
    return render(request,"faculty/login.html",context)

def fetch_login(request):
    username=request.POST.get("uname")
    password=request.POST.get("pwd")
    print(username,password)
    return render(request,"faculty/facultyhome.html")


def get_feedback(request):
    return render(request,"faculty/feedback.html")