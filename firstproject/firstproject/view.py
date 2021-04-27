from django.http import HttpResponse

def registeration(request):
    return HttpResponse ("<h1>Welcome to registeration</h1>")

def addition(request):
    return HttpResponse("<h1>Welcome to Addition</h1>")

def subtraction(request):
    return HttpResponse("<h1>Welcome to subtraction</h1>")

def multiplication(request):
    return HttpResponse("<h1>Welcome to multiplication</h1>")

def division(request):
    return HttpResponse("<h1>Welcome to division</h1>")