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

