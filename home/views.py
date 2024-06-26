from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from markdown.core import markdown
from rest_framework import generics
from django.utils.timezone import now
from collections import defaultdict
from django.contrib.auth.decorators import login_required
from home.models.user import User
from home.models.flashcards import FlashcardSet, Flashcard
from utils import grade_writing_task
from .serializers import QuestionSerializer
from django.http import HttpResponseBadRequest
from django.db import IntegrityError
from .const.format import format
from .const.exam import exam_list
from .const.skill import skill_list
from .const.time_limit import time_limit_list
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .models.question import Question
from .models.user_test_result import UserTestResult
from .models.test_history import TestHistory
from .models.user_post import Post
from .forms import PostForm, CommentForm, FlashcardSetForm, FlashcardFormSet
from random import sample


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


@login_required
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
    questions = Question.objects.filter(skill=skill, exam=exam, level=level)

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
    format_names = {k: v for d in format for k, v in d.items()}
    if request.method == 'POST':
        skill = request.POST.get('skill')
        exam = request.POST.get('exam')
        level = request.POST.get('level')
        format_value = request.POST.get('format', None)
        time_limit = request.POST.get('timeLimit')

        # Filter answers submitted and fetch question IDs
        submitted_answers = {int(key.split('_')[1]): int(value) for key, value in request.POST.items() if
                             key.startswith('answer')}
        question_ids = submitted_answers.keys()

        user_writing_answers = {}
        question_ids = user_writing_answers.keys()

        # Iterate over all POST keys to find keys related to writing answers
        for key, value in request.POST.items():
            if key.startswith('writing_answer_'):
                # Extract the question ID from the key
                question_id = int(key.split('_')[-1])
                # Add the writing answer to the dictionary
                user_writing_answers[question_id] = value

        # Fetch all questions for the given skill and exam, and optionally by format

        if not level:
            level = '2'

        # Filter based on query strings
        all_questions = Question.objects.filter(skill=skill, exam=exam, level=level)

        # Only apply the format filter if format_value is provided and not empty
        if format_value:
            try:
                format_values = list(map(int, format_value.split(',')))  # Convert each value to an integer
                all_questions = all_questions.filter(format__in=format_values)
            except ValueError:
                # Handle the case where conversion to integer fails
                pass  # You might want to log this case or handle it appropriately

        user_score = 0
        total_score = 0
        user_choices = {}
        correct_answers = {}

        # Initialize format statistics
        format_statistics = defaultdict(lambda: {'correct': 0, 'wrong': 0, 'unchosen': 0})

        # Iterate over fetched questions
        for question in all_questions:
            correct_option_num = question.correct_option
            user_choice = submitted_answers.get(question.question_id)
            question_format = question.format

            # For statistics, use the description as the key
            format_key = format_names.get(question_format, "Unknown Format")

            # Update user choices and correct answers tracking
            user_choices[question.question_id] = user_choice
            correct_answers[question.question_id] = correct_option_num

            # Calculate scores and stats based on user answers
            if user_choice is None:
                format_statistics[format_key]['unchosen'] += 1
                total_score += question.score
            elif user_choice == correct_option_num:
                user_score += question.score
                total_score += question.score
                format_statistics[format_key]['correct'] += 1
            else:
                format_statistics[format_key]['wrong'] += 1
                total_score += question.score

        if format_value is None:
            test_type = 2
        else:
            test_type = 1

        # User and TestHistory handling
        user = request.user if request.user.is_authenticated else User.objects.get(username='undefinedUser')
        test_history = TestHistory.objects.create(
            user=user,
            exam_name=exam,
            skill_name=skill,
            test_date=now(),
            user_score=user_score,
            total_score=total_score,
            format_name=format_value,
            time_limit=time_limit,
            format_statistics=dict(format_statistics),
            test_type=test_type,
        )

        # Prepare and execute bulk create for user test results
        # Filter questions to include only those with a provided answer
        user_test_results = [
            UserTestResult(
                user_answer=submitted_answers.get(question.question_id) if submitted_answers is not None else None,
                question_id=question,
                test_history_id=test_history,
                user_writing_answer=user_writing_answers.get(
                    question.question_id) if user_writing_answers is not None else None,
                suggested_writing_answer=grade_writing_task(question, user_writing_answers.get(
                    question.question_id) if user_writing_answers is not None else None) if question.format in [
                    24] else None
            )
            for question in all_questions
        ]

        UserTestResult.objects.bulk_create(user_test_results)
        return HttpResponseRedirect(f'/test-history/{test_history.test_history_id}')


@login_required
def get_test_history(request, test_history_id):
    test_history = get_object_or_404(TestHistory, test_history_id=test_history_id)
    format_names_list = format
    format_names = {k: v for d in format for k, v in d.items()}
    # Getting info
    total_score = round(test_history.total_score)
    user_score = round(test_history.user_score)
    exam = test_history.exam_name
    skill = test_history.skill_name
    time_limit = test_history.time_limit
    format_value = test_history.format_name
    format_statistics = test_history.format_statistics
    level = test_history.level

    exam_name = exam_list[int(exam) - 1][int(exam)]
    skill_name = skill_list[int(skill) - 1][int(skill)]

    if level is None:
        level = '2'

        # Filter based on query strings
    all_questions = Question.objects.filter(skill=skill, exam=exam, level=level)
    # Only apply the format filter if format_value is provided and not empty
    if format_value:
        try:
            format_values = list(map(int, format_value.split(',')))  # Convert each value to an integer
            all_questions = all_questions.filter(format__in=format_values)
        except ValueError:
            # Handle the case where conversion to integer fails
            pass  # You might want to log this case or handle it appropriately

    user_choices = UserTestResult.objects.filter(test_history_id=test_history_id)
    user_writing_answers = {result.question_id_id: result.user_writing_answer for result in user_choices}
    suggested_writing_answers = {result.question_id_id: markdown(result.suggested_writing_answer if
                                                                 result.suggested_writing_answer is not None else '')
                                 for result in user_choices}
    user_choices = {result.question_id_id: result.user_answer for result in user_choices}

    # Dictionary to store correct options for each question
    correct_answers = {question.question_id: question.correct_option for question in all_questions}

    # Context for rendering results
    context = {
        "page_name": "Your Results",
        "test_date": test_history.test_date,
        "exam_name": exam_name,
        "skill_name": skill_name,
        "total_score": total_score,
        "user_score": user_score,
        "time_limit": time_limit,
        "exam": exam,
        "skill": skill,
        "format_names": format_names_list,
        "questions": all_questions,
        "user_choices": user_choices,
        "correct_answers": correct_answers,
        "format_statistics": format_statistics,
        "user_writing_answers": user_writing_answers,
        "suggested_writing_answers": suggested_writing_answers,
        # Convert default dictionary to a regular dictionary for template usage
    }
    return render(request, 'final_grade_result.html', context)


@login_required
def user_profile(request, user_id):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_id)

    # Access the custom user fields
    first_name = request.user.first_name
    last_name = request.user.last_name
    date_of_birth = request.user.date_of_birth
    gender = request.user.gender
    phone_number = request.user.phone_number
    username = request.user.username
    test_histories = TestHistory.objects.filter(user=user)

    context = {
        'test_histories': test_histories,
        'exam_list': exam_list,  # Assuming exam_list is defined elsewhere
        'page_name': first_name + ' ' + last_name,
        'user_id': user_id,
        'first_name': first_name,
        'last_name': last_name,
        'date_of_birth': date_of_birth,
        'gender': gender,
        'phone_number': phone_number,
        'username': username,
    }
    return render(request, 'user_profile.html', context)


@login_required
def user_test_history(request, user_id):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_id)

    # Access the custom user fields
    first_name = request.user.first_name
    last_name = request.user.last_name
    test_histories = TestHistory.objects.filter(user=user)

    context = {
        'test_histories': test_histories,
        'exam_list': exam_list,  # Assuming exam_list is defined elsewhere
        'page_name': "My Test History",
        'user_id': user_id,
        'first_name': first_name,
        'last_name': last_name,
    }
    return render(request, 'user_test_history.html', context)


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts, 'page_name': "Forum"})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'form': form, 'comments': comments,
                                                'pk': pk, 'page_name': "Post"})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form, 'page_name': "Edit Post"})


def flashcard_set_list(request):
    # Retrieve all flashcard sets from the database
    flashcard_sets = FlashcardSet.objects.all()

    # Pass the flashcard sets to the template for rendering
    return render(request, 'flashcard_set_list.html', {'flashcard_sets': flashcard_sets,
                                                       "page_name": "Flashcards"})


def flashcard_set_detail(request, pk):
    flashcard_set = get_object_or_404(FlashcardSet, pk=pk)
    flashcards = Flashcard.objects.filter(set_id=pk)
    all_flashcard_sets = FlashcardSet.objects.all()
    if len(all_flashcard_sets) >= 3:
        # Select 3 random flashcard sets
        random_flashcard_sets = sample(list(all_flashcard_sets), 3)
    else:
        random_flashcard_sets = all_flashcard_sets

    return render(request, 'flashcard_set_detail.html', {'flashcard_set': flashcard_set, 'flashcards': flashcards,
                                                         "page_name": "Flashcards",
                                                         'random_flashcard_sets': random_flashcard_sets, })


@login_required()
def flashcard_set_new(request):
    if request.method == 'POST':
        set_form = FlashcardSetForm(request.POST)
        flashcard_formset = FlashcardFormSet(request.POST)
        if set_form.is_valid() and flashcard_formset.is_valid():
            # Save the flashcard set
            flashcard_set = set_form.save(commit=False)
            flashcard_set.user = request.user
            flashcard_set.save()

            # Save the flashcards associated with the flashcard set
            for form in flashcard_formset:
                flashcard = form.save(commit=False)
                flashcard.set = flashcard_set
                flashcard.save()

            return redirect('flashcard_set_detail.html', set_id=flashcard_set.id)
    else:
        set_form = FlashcardSetForm()
        flashcard_formset = FlashcardFormSet()
    return render(request, 'flashcard_set_new.html', {'set_form': set_form, 'flashcard_formset': flashcard_formset})
