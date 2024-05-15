from collections import defaultdict
import google.generativeai as genai

from const.prompt import *
from hanjahero.settings import GEMINI_SK
from home.models.question_meta_data import QuestionMetaData

genai.configure(api_key=GEMINI_SK)


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
        format_item[0].format = format_constants[format_id - 1]
        reordered_questions.extend(questions_by_format.get(format_id - 1, []))

    return reordered_questions


def get_description_by_key(key, format_names):
    for format_dict in format_names:
        if key in format_dict:
            return format_dict[key]
    return "Description not found"


def grade_writing_task(question, user_writing_answer):
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    if question.format == 23:
        return ''# model.generate_content(basic_53_prompt + user_writing_answer).candidates[0].content.parts[0].text
    else:
        topic = QuestionMetaData.objects.get(question=question).question_meta_text
        return model.generate_content(basic_54_prompt.replace('$topic', topic) + user_writing_answer).candidates[0].content.parts[0].text

