from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from rest_framework import generics

from .models.user import User
from .serializers import QuestionSerializer
from django.http import HttpResponseBadRequest
from django.db import IntegrityError
from .const.format import format
from .const.exam import exam_list
from .const.skill import skill_list
from .const.time_limit import time_limit_list
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .models.question import Question
from .models.user_test_result import UserTestResult
from .models.test_history import TestHistory


def home(request):
    context = {"page_name": "Hanja Hero", }
    return render(request, 'home.html', context)


def log_in(request):
    context = {
        "page_name": "Log In",
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)

            # Redirect to a success page or home page
            return redirect('/home/', context)
        elif user is None:
            context['error_message'] = "Invalid credentials. Log in again."
            # Return an error message or render the login page again with error
            return render(request, 'login.html', context)
    else:
        # Render the login page
        return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/home/')


def sign_up(request):
    if request.method == 'POST':
        try:
            # Retrieve form data from POST request
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            date_of_birth = request.POST.get('date_of_birth')
            gender = request.POST.get('gender')
            phone_number = request.POST.get('phone_number')
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Create a new User object and save it to the database
            new_user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                gender=gender,
                phone_number=phone_number,
                username=username,
                password=make_password(password)
            )
            login(request, new_user)
            # Redirect to a success page or do something else
            return redirect('home')  # Replace 'success_page' with the URL name of your success page

        except IntegrityError as e:
            # Render the form again with the error message
            return render(request, 'register.html', {'error_message': e, 'page_name': "Sign Up"})

    # For GET request, render the sign-up form
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


def get_test(request):
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
        "page_name": "In Test",
        "questions": questions,
        "exam": exam_name,
        "exam_number": exam,
        "skill": skill_name,
        "skill_number": skill,
        "time_limit": time_limit,
        "format_param": format_param,
        "format": format,
        "skill_time": skill,
    }

    return render(request, 'layout/test_base.html', data)


def grade_test_view(request):
    if request.method == 'POST':
        # Process the form data efficiently
        skill = request.POST.get('skill')
        exam = request.POST.get('exam')
        format_value = request.POST.get('format', None)  # Default to None if not provided

        # Filter only the relevant 'exampleRadios' keys and extract their answers
        submitted_answers = {int(key.split('_')[1]): int(value) for key, value in request.POST.items() if key.startswith('answer')}

        # Fetch relevant questions in one go to minimize database hits
        question_ids = submitted_answers.keys()
        questions = Question.objects.filter(question_id__in=question_ids)

        total_score = 0
        user_choices = {}
        correct_answers = {}

        # Process questions and calculate total score
        for question in questions:
            submitted_answer = submitted_answers.get(question.question_id)
            correct_option_num = question.correct_option  # Assuming correct option is directly comparable to
            # submitted answer

            user_choices[question.question_id] = submitted_answer
            correct_answers[question.question_id] = correct_option_num

            if submitted_answer == correct_option_num:
                total_score += question.score

        user = request.user if request.user.is_authenticated else User.objects.get(username='undefinedUser')

        # Create test history once, outside of the loop
        test_history = TestHistory.objects.create(
            user=user,
            exam_name=exam,
            skill_name=skill,
            test_date=datetime.now(),
            score=total_score,
            format_name=format_value
        )

        # Prepare bulk create for user test results
        user_test_results = [UserTestResult(
            user_answer=submitted_answers[question.question_id],
            question_id=question,
            test_history_id=test_history
        ) for question in questions]

        UserTestResult.objects.bulk_create(user_test_results)

        # Assuming `exam_list` and `skill_list` are defined elsewhere and are valid
        exam_name = exam_list[int(exam) - 1][int(exam)]
        skill_name = skill_list[int(skill) - 1][int(skill)]

        user_finished_questions = Question.objects.filter(skill=skill, exam=exam)

        context = {
            "page_name": "Your Results",
            "score": total_score,
            "questions": questions,
            "user_finished_questions": user_finished_questions,
            "exam": exam_name,
            "exam_number": exam,
            "skill": skill_name,
            "skill_number": skill,
            "user_choices": user_choices,
            "correct_answers": correct_answers,
        }

        return render(request, 'final_grade_result.html', context)

    return HttpResponseRedirect('/')
