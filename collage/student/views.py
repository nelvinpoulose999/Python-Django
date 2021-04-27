from django.shortcuts import render
from .form import StudentRegisterationForm,StudentLoginForm

# Create your views here.
# registeration
def get_student_registeration(request):
    form=StudentRegisterationForm()
    context={}
    context["form"]=form
    return render(request, "student/studentregisteration.html",context)


def fetch_data(request):
    firstname=request.POST.get("fname")
    username=request.POST.get("uname")
    password=request.POST.get("pwd")
    phonenumber = request.POST.get("pnum")
    course = request.POST.get("cour")
    print(firstname,username,password,phonenumber,course)
    return render(request, "student/studentlogin.html")

# login
def get_log(request):
    form=StudentLoginForm()
    context={}
    context["form"] = form
    return render(request, "student/studentlogin.html",context)

def fetch_login(request):
    username=request.POST.get("uname")
    password=request.POST.get("pwd")
    print(username,password)
    return render(request, "student/studenthome.html")



def get_feed(request):
    return render(request, "student/postfeedback.html")
