from django.core.management.base import BaseCommand
from home.models.question import Question


class Command(BaseCommand):
    help = 'Populate time_limit field based on skill'

    def handle(self, *args, **kwargs):
        for obj in Question.objects.all():
            if obj.skill == 1:
                obj.time_limit = 1
            elif obj.skill == 2:
                obj.time_limit = 2
            elif obj.skill == 3:
                obj.time_limit = 3
            # Add more conditions as needed
            obj.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated time_limit field'))
