import json
from django.core.management.base import BaseCommand
from home.models.question import Question
from home.models.question_meta_data import QuestionMetaData


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file']) as f:
            data_list = json.load(f)

        for data in data_list:
            # Retrieve QuestionMetaData instance if ID is provided
            question_meta_data_id = data.pop('question_meta_data', None)
            question_meta_data = None
            if question_meta_data_id is not None:
                try:
                    question_meta_data = QuestionMetaData.objects.get(pk=question_meta_data_id)
                except QuestionMetaData.DoesNotExist:
                    # Handle the case where the QuestionMetaData with the provided ID doesn't exist
                    self.stdout.write(self.style.ERROR(f"QuestionMetaData with ID {question_meta_data_id} does not exist."))

            # Create or update the Question instance
            question, created = Question.objects.update_or_create(question_id=data['question_id'], defaults={**data, 'question_meta_data': question_meta_data})