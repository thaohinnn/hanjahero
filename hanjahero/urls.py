"""
URL configuration for hanjahero project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('abouttheTOPIKexam/', views.abouttheTOPIKexam, name='abouttheTOPIKexam'),
    path('examdates/', views.TOPIKexamdates, name='TOPIKexamdates'),
    path('mocktestslibrary/', views.mocktestslibrary, name='mocktestslibrary'),
    path('practicetestslibrary/', views.practicetestslibrary, name='practicetestslibrary'),
    path('mocktestslibrary/topik1/', views.topik1mocklibrary, name='topik1mocklibrary'),
    path('mocktestslibrary/topik2/', views.topik2mocklibrary, name='topik2mocklibrary'),
    path('test/', views.test, name='test'),
    path('recover/', views.passwordrecover, name='passwordrecover'),
    path('terms/', views.userterms, name='userterms')
]
