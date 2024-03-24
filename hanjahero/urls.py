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
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('aboutus/', views.about_us, name='aboutus'),
    path('abouttheTOPIKexam/', views.about_the_topik_exam, name='abouttheTOPIKexam'),
    path('examdates/', views.topik_exam_dates, name='TOPIKexamdates'),
    path('mocktestslibrary/', views.mock_tests_library, name='mocktestslibrary'),
    path('practicetestslibrary/', views.practice_tests_library, name='practicetestslibrary'),
    path('mocktestslibrary/topik1/', views.topik1_mock_library, name='topik1mocklibrary'),
    path('mocktestslibrary/topik2/', views.topik2_mock_library, name='topik2mocklibrary'),
    path('test/', views.test, name='test'),
    path('recover/', views.password_recover, name='passwordrecover'),
    path('terms/', views.user_terms, name='userterms'),
    path('practicetestslibrary/topik1/', views.topik1_practice_library, name='topik1practicelibrary'),
    path('practicetestslibrary/topik2/', views.topik2_practice_library, name='topik2practicelibrary'),
]
