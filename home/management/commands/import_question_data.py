import json
from django.core.management.base import BaseCommand
from home.models.question import Question
from home.models.question_meta_data import QuestionMetaData  # Import Question and QuestionMetaData models
from django.db import connection


def reset_auto_increment():
    with connection.cursor() as cursor:
        cursor.execute("ALTER TABLE home_question AUTO_INCREMENT = 1;")


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file'], 'r') as f:
            data_list = json.load(f)

        for data in data_list:
            # Get the question_meta_data id from the JSON data
            question_meta_data_id = data.pop('question_meta_data', None)

            # Check if question_meta_data_id exists
            if question_meta_data_id is not None:
                try:
                    # Try to get the QuestionMetaData instance
                    question_meta_data = QuestionMetaData.objects.get(question_meta_id=question_meta_data_id)
                except QuestionMetaData.DoesNotExist:
                    # If the QuestionMetaData instance does not exist, set it to None
                    question_meta_data = None
                    print(f"QuestionMetaData with ID {question_meta_data_id} does not exist.")

            # Create the Question object with the remaining data
            question = Question.objects.create(question_meta_data=question_meta_data, **data)
            print(f"Question created: {question}")