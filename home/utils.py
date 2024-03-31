from collections import defaultdict


def reorder_questions_by_format(questions, format_constants):
    # Create a defaultdict to store questions grouped by format
    questions_by_format = defaultdict(list)

    # Iterate over each question
    for question in questions:
        # Get the format of the question
        question_format = question.format

        # Add the question to the list corresponding to its format
        questions_by_format[question_format].append(question)

    # Sort the format constants alphabetically
    sorted_formats = sorted(format_constants, key=lambda x: list(x.values())[0])

    # Reorder the questions based on the sorted formats
    reordered_questions = []
    for format_item in sorted_formats:
        format_id = list(format_item.keys())[0]
        reordered_questions.extend(questions_by_format.get(format_id, []))

    return reordered_questions


def reorder_format(questions, format_constants):
    # Create a defaultdict to store questions grouped by format
    questions_by_format = defaultdict(list)

    # Iterate over each question
    for question in questions:
        # Get the format of the question
        question_format = question.format

        # Add the question to the list corresponding to its format
        questions_by_format[question_format].append(question)

    # Sort the format constants alphabetically
    sorted_formats = sorted(format_constants, key=lambda x: list(x.values())[0])

    return sorted_formats


print('s')
