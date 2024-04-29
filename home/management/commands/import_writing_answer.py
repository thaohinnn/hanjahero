import json
from django.core.management.base import BaseCommand
from home.models.question import Question


class Command(BaseCommand):
    help = 'Import data from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('writing_answers.json', type=str, help='home/static/data/writing_answers.json')

    def handle(self, *args, **kwargs):
        json_file_path = kwargs['writing_answers.json']

        # Read the JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        # Iterate over the JSON data and import it into the database
        for item in data:
            writing_answer = item.get('writing_answer', None)
            question_id = item.get('question_id', None)

            # Create or update database records
            # You may need to adjust this part based on your model structure
            # For example, assuming YourModel has fields 'writing_answer' and 'question_id'
            # Replace 'YourModel' with the actual name of your model class
            Question.objects.update_or_create(question_id=question_id, defaults={'writing_answer': writing_answer})

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
