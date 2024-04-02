from django.shortcuts import render
from rest_framework import generics
from .serializers import QuestionSerializer
from .models.question import Question
from .utils import reorder_questions_by_format
from django.http import HttpResponseBadRequest
from .const.format import format
from .const.exam import exam_list
from .const.skill import skill_list
from .const.level import level_list
from .const.time_limit import time_limit_list


def home(request):
    page_name = {"page_name": "Hanja Hero"}
    return render(request, 'home.html', page_name)


def log_in(request):
    page_name = {"page_name": "Log In"}
    return render(request, 'login.html', page_name)


def sign_up(request):
    page_name = {"page_name": "Sign Up"}
    return render(request, 'register.html', page_name)


def user_terms(request):
    page_name = {"page_name": "User Terms"}
    return render(request, 'user_terms.html', page_name)


def about_us(request):
    page_name = {"page_name": "About Us"}
    return render(request, 'about_us.html', page_name)


def about_the_topik_exam(request):
    page_name = {"page_name": "About TOPIK"}
    return render(request, 'about_the_topik.html', page_name)


def topik_exam_dates(request):
    page_name = {"page_name": "TOPIK Exam Dates"}
    return render(request, 'topik_exam_dates.html', page_name)


def mock_tests_library(request):
    page_name = {"page_name": "Mock Tests Library"}
    return render(request, 'mock_tests_library.html', page_name)


def practice_tests_library(request):
    page_name = {"page_name": "Practice Tests Library"}
    return render(request, 'practice_tests_library.html', page_name)


def topik1_mock_library(request):
    page_name = {"page_name": "TOPIK I Mock Tests"}
    return render(request, 'topik1_mock_library.html', page_name)


def topik2_mock_library(request):
    page_name = {"page_name": "TOPIK II Mock Tests"}
    return render(request, 'topik2_mock_library.html', page_name)


def topik1_practice_library(request):
    page_name = {"page_name": "TOPIK I Practice Tests"}
    return render(request, 'topik1_practice_library.html', page_name)


def topik2_practice_library(request):
    page_name = {"page_name": "TOPIK II Practice Tests"}
    return render(request, 'topik2_practice_library.html', page_name)


def password_recover(request):
    page_name = {"page_name": "Forgot Password?"}
    return render(request, 'recover.html', page_name)


######DATABASE VIEWSETS
class QuestionView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SingleQuestionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        # Retrieve a single question based on some condition, such as primary key
        question_id = self.kwargs.get('pk')
        if question_id is not None:
            queryset = Question.objects.filter(pk=question_id)
        else:
            queryset = Question.objects.none()
        return queryset


def get_mock_test(request):
    ##### GET DATA
    format_constants = format
    # get query string parameters from the request
    skill = request.GET.get('skill')
    exam = request.GET.get('exam')

    # Error-handling
    if not skill or not exam:
        return HttpResponseBadRequest("Sorry, this test is not available.")

    # filter based on query strings
    questions = Question.objects.filter(skill=skill, exam=exam)

    ######## TRANSFORM DATA HERE
    # reorder questions
    questions = reorder_questions_by_format(questions, format_constants)

    data = {
        "page_name": "TOPIK II Practice Tests",
        "questions": questions,
        "format": format_constants,
    }

    return render(request, 'layout/test.html', data)


def get_mock_test_test(request):
    ##### GET DATA
    # get query string parameters from the request
    skill = request.GET.get('skill')
    exam = request.GET.get('exam')
    level = request.GET.get('level')

    # Error-handling
    if not skill or not exam or not level:
        return HttpResponseBadRequest("Sorry, this test is not available.")

    # filter based on query strings
    questions = Question.objects.filter(skill=skill, exam=exam)
    format_constants = format

    ######## TRANSFORM DATA HERE
    # reorder questions
    exam_name = exam_list[int(exam) - 1][int(exam)]
    skill_name = skill_list[int(skill) - 1][int(skill)]
    time_limit = time_limit_list[int(skill) - 1][int(skill)]

    questions = reorder_questions_by_format(questions, format_constants)

    data = {
        "page_name": "TOPIK II Practice Tests",
        "questions": questions,
        "format": format_constants,
        "exam": exam_name,
        "skill": skill_name,
        "time_limit": time_limit,

    }

    return render(request, 'layout/test2.html', data)



