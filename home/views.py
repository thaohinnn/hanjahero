from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def test(request):
    return render(request, 'test.html')

def signup(request):
    return render(request, 'register.html')

def aboutus(request):
    return render(request, 'aboutus.html')