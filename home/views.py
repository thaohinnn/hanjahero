from django.shortcuts import render


def home(request):
    page_name =  {"page_name" : "Hanja Hero"}
    return render(request, 'home.html', page_name)


def log_in(request):
    page_name =  {"page_name" : "Log In"}
    return render(request, 'login.html', page_name)


def sign_up(request):
    page_name =  {"page_name" : "Sign Up"}
    return render(request, 'register.html', page_name)


def user_terms(request):
    page_name =  {"page_name" : "User Terms"}
    return render(request, 'user_terms.html', page_name)


def about_us(request):
    page_name =  {"page_name" : "About Us"}
    return render(request, 'about_us.html', page_name)


def about_the_topik_exam(request):
    page_name =  {"page_name" : "About TOPIK"}
    return render(request, 'about_the_topik.html', page_name)


def topik_exam_dates(request):
    page_name =  {"page_name" : "TOPIK Exam Dates"}
    return render(request, 'topik_exam_dates.html', page_name)


def mock_tests_library(request):
    page_name =  {"page_name" : "Mock Tests Library"}
    return render(request, 'mock_tests_library.html', page_name)


def practice_tests_library(request):
    page_name =  {"page_name" : "Practice Tests Library"}
    return render(request, 'practice_tests_library.html', page_name)


def topik1_mock_library(request):
    page_name =  {"page_name" : "TOPIK I Mock Tests"}
    return render(request, 'topik1_mock_library.html', page_name)


def topik2_mock_library(request):
    page_name =  {"page_name" : "TOPIK II Mock Tests"}
    return render(request, 'topik2_mock_library.html', page_name)


def topik1_practice_library(request):
    page_name =  {"page_name" : "TOPIK I Practice Tests"}
    return render(request, 'topik1_practice_library.html', page_name)


def test(request):
    page_name =  {"page_name" : "TOPIK II Practice Tests"}
    return render(request, 'test.html', page_name)


def password_recover(request):
    page_name =  {"page_name" : "Forgot Password?"}
    return render(request, 'recover.html', page_name)
