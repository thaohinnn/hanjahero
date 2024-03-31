from django.urls import path
from . import views

urlpatterns = [
    path('questions', views.QuestionView.as_view()),
    path('questions/<int:pk>', views.SingleQuestionView.as_view(), name='retrieve_update_destroy')
]
