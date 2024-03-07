from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'register.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def abouttheTOPIKexam(request):
    return render(request, 'abouttheTOPIKexam.html')

def mocktestslibrary(request):
    return render(request, 'mocktestslibrary.html')

def practicetestslibrary(request):
    return render(request, 'practicetestslibrary.html')

def topik1mocklibrary(request):
    return render(request, 'topik1mocklibrary.html')

def test(request):
    return render(request, 'test.html')