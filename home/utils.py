from collections import defaultdict
from .models.question import Question


def reorder_questions_by_format(questions, format_constants):
    # Create a defaultdict to store questions grouped by format
    questions_by_format = defaultdict(list)

    # Iterate over each question
    for question in questions:
        # Add the question to the list corresponding to its format
        questions_by_format[question.format].append(question)

    # Todo Add sorting questions_by_format by key here

    # Flat questions_by_format into reordered_questions
    reordered_questions = []
    for format_id, format_item in questions_by_format.items():
        # only set format string for first question in each format questions group.
        format_item[0].format = format_constants[format_id-1]
        reordered_questions.extend(questions_by_format.get(format_id-1, []))

    return reordered_questions


def grade_test(user_responses):
    total_score = 0

    for response in user_responses:
        question_id = response['question_id']
        selected_option = response['selected_option']

        # Retrieve the correct option from the database
        try:
            question = Question.objects.get(question_id=question_id)
            correct_option = question.correct_option
            score = question.score
        except Question.DoesNotExist:
            # Handle the case where the question doesn't exist
            continue

        # Check if the user's answer matches the correct option
        if selected_option == correct_option:
            total_score += score

    return total_score
