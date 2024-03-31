import json
from django.core.management.base import BaseCommand
from home.models.question_meta_data import QuestionMetaData


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file']) as f:
            data_list = json.load(f)

        for item in data_list:
            question_meta_id = item.get('question_meta_id')
            question_meta_text = item.get('question_meta_text')

            # Create or update QuestionMetaData object
            obj, created = QuestionMetaData.objects.update_or_create(
                question_meta_id=question_meta_id,
                defaults={'question_meta_text': question_meta_text}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created QuestionMetaData with ID {obj.question_meta_id}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated QuestionMetaData with ID {obj.question_meta_id}'))
