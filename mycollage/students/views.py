from django.shortcuts import render,redirect
from .forms import StudentRegisterForm,StudentLoginForm


# Create your views here.

# Student Registeration

def get_registeration(request):
    # student register form
    context = {}
    form = StudentRegisterForm()
    context['form'] = form
    if request.method=='POST':
        form=StudentRegisterForm(request.POST)
        if form.is_valid():
            Firstname=form.cleaned_data.get('Firstname')
            Lastname = form.cleaned_data.get('Lastname')
            Course = form.cleaned_data.get('Course')
            Phonenumber = form.cleaned_data.get('Phonenumber')
            Age = form.cleaned_data.get('Age')
            Password = form.cleaned_data.get('Password')
            print(Firstname,Lastname,Course,Phonenumber,Age,Password)
            return redirect('login')
        else:
            form = StudentRegisterForm(request.POST)
            context['form'] = form
            return render(request, 'students/studregisteration.html', context)

    return render(request,'students/studregisteration.html',context)

def fetch_register(request):
    Firstname=request.POST.get("fname")
    Lastname=request.POST.get("lname")
    Course=request.POST.get("cours")
    Phonenumber=request.POST.get("pnum")
    Password=request.POST.get("psw")
    print(Firstname,Lastname,Course,Phonenumber,Password)
    return render(request,"students/studlogin.html")

# Student Login

def get_login(request):
    # student login form
    context={}
    form=StudentLoginForm()
    context['form']=form
    if request.method=='POST':
        form=StudentLoginForm(request.POST)
        if form.is_valid():
            Username=form.cleaned_data.get('Username')
            Password=form.cleaned_data.get('Password')
            print(Username,Password)
            return redirect("home")
    return render(request,"students/studlogin.html",context)

def fetch_login(request):
    Username=request.POST.get('uname')
    Password=request.POST.get('psw')
    print(Username,Password)
    return render(request,'students/studhome.html')

def get_home(request):
    return render(request,'students/studhome.html')