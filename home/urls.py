from django.urls import path
from . import views

urlpatterns = [
    path('questions', views.QuestionView.as_view()),
    path('<int:pk>', views.QuestionView.as_view(), name='retrieve_update_destroy')
]
