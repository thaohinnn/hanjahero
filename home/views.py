from django.shortcuts import render


def home(request):
    page_name =  {"page_name" : "Hanja Hero"}
    return render(request, 'home.html', page_name)


def login(request):
    page_name =  {"page_name" : "Log In"}
    return render(request, 'login.html', page_name)


def signup(request):
    page_name =  {"page_name" : "Sign Up"}
    return render(request, 'register.html', page_name)


def userterms(request):
    page_name =  {"page_name" : "User Terms"}
    return render(request, 'userterms.html', page_name)


def aboutus(request):
    page_name =  {"page_name" : "About Us"}
    return render(request, 'aboutus.html', page_name)


def abouttheTOPIKexam(request):
    page_name =  {"page_name" : "About TOPIK"}
    return render(request, 'abouttheTOPIKexam.html', page_name)


def TOPIKexamdates(request):
    page_name =  {"page_name" : "TOPIK Exam Dates"}
    return render(request, 'TOPIKexamdates.html', page_name)


def mocktestslibrary(request):
    page_name =  {"page_name" : "Mock Tests Library"}
    return render(request, 'mocktestslibrary.html', page_name)


def practicetestslibrary(request):
    page_name =  {"page_name" : "Practice Tests Library"}
    return render(request, 'practicetestslibrary.html', page_name)


def topik1mocklibrary(request):
    page_name =  {"page_name" : "TOPIK I Mock Tests"}
    return render(request, 'topik1mocklibrary.html', page_name)


def topik2mocklibrary(request):
    page_name =  {"page_name" : "TOPIK II Mock Tests"}
    return render(request, 'topik2mocklibrary.html', page_name)


def topik1practicelibrary(request):
    page_name =  {"page_name" : "TOPIK I Practice Tests"}
    return render(request, 'topik1practicelibrary.html', page_name)


def test(request):
    page_name =  {"page_name" : "TOPIK II Practice Tests"}
    return render(request, 'test.html', page_name)


def passwordrecover(request):
    page_name =  {"page_name" : "Forgot Password?"}
    return render(request, 'recover.html', page_name)
