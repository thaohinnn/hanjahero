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
from django.urls import path, include
from hanjahero import settings
from home import views


if settings.DEBUG:
    import debug_toolbar

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
    path('recover/', views.password_recover, name='passwordrecover'),
    path('terms/', views.user_terms, name='userterms'),
    path('practicetestslibrary/topik1/', views.topik1_practice_library, name='topik1practicelibrary'),
    path('practicetestslibrary/topik2/', views.topik2_practice_library, name='topik2practicelibrary'),
    path('test/', views.get_test, name='mock_test'),
    path('practice/', views.get_test, name='mock_test'),
    path('test-result/', views.grade_test_view, name='grade_test_view'),
    path('logout/', views.logout_view, name='logout'),
    path('test-history/', views.get_all_test_history, name='get-next-id'),
    path('test-history/<int:test_history_id>', views.get_test_history, name='get-next-id'),
    path('profile/<int:user_id>', views.user_profile, name='user_profile'),  # For function-based view

    path('api/', include('home.urls')),

    path(r'__debug__/', include(debug_toolbar.urls)),
]
