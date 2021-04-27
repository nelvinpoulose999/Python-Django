from django.shortcuts import render

# Create your views here.

# Faculty registeration

def get_registeration(request):
    return render(request,'facultys/facuregisteration.html')

def fetch_register(request):
    Firstname=request.POST.get('fname')
    Lastname=request.POST.get('lname')
    Course=request.POST.get('cours')
    Phonenumber=request.POST.get('pnum')
    Password=request.POST.get('psw')
    print(Firstname,Lastname,Course,Phonenumber,Password)
    return render(request,'facultys/faculogin.html')

# Faculty Login

def get_login(request):
    return render(request,'facultys/faculogin.html')

def fetch_login(request):
    Username=request.POST.get("uname")
    Password=request.POST.get("pwd")
    print(Username,Password)
    return render(request,'facultys/facuhome.html')