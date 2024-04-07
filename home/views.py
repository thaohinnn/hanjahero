from django.shortcuts import render
from rest_framework import generics
from .serializers import QuestionSerializer
from .models.question import Question
from .utils import grade_test
from django.http import HttpResponseBadRequest
from .const.format import format
from .const.exam import exam_list
from .const.skill import skill_list
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


def get_mock_test_test(request):
    # Get query string parameters from the request
    skill = request.GET.get('skill')
    exam = request.GET.get('exam')
    level = request.GET.get('level')
    format_param = request.GET.get('format')

    # Error-handling
    if not skill or not exam:
        return HttpResponseBadRequest("Sorry, this test is not available.")

    # Set default level to '2' if not specified
    if not level:
        level = '2'

    # Filter based on query strings
    questions = Question.objects.filter(skill=skill, exam=exam)

    # Apply additional filtering based on the 'format' parameter if provided
    if format_param:
        format_values = format_param.split(',')  # Split format parameter into a list of values
        questions = questions.filter(format__in=format_values)

    # Transform data
    exam_name = exam_list[int(exam) - 1][int(exam)]
    skill_name = skill_list[int(skill) - 1][int(skill)]
    time_limit = time_limit_list[int(skill) - 1][int(skill)]

    data = {
        "page_name": "TOPIK II Practice Tests",
        "questions": questions,
        "exam": exam_name,
        "skill": skill_name,
        "time_limit": time_limit,
        "format_param": format_param,
        "format": format,
        "skill_time": skill,
    }

    return render(request, 'layout/test_base.html', data)


def grade_test_view(request):
    if request.method == 'POST':
        total_score = 0
        for key, value in request.POST.items():
            if key.startswith('question_'):  # Assuming question fields start with 'question_'
                question_id = int(key.split('_')[1])
                selected_option = int(value)
                # Now you have the question_id and selected_option, you can process it further
                # For simplicity, let's assume you have a list of dictionaries containing user responses
                user_responses = [{'question_id': question_id, 'selected_option': selected_option}]
                total_score += grade_test(user_responses)
        return render(request, 'grade_result.html', {'total_score': total_score})
    else:
        pass
        # Handle GET request (show the form to submit test responses)
        ##return render(request, 'test_form.html')



