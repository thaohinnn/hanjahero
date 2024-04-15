from django.core.management.base import BaseCommand
from home.models.test_history import TestHistory


class Command(BaseCommand):
    help = 'Assigns test type based on the format_name'

    def handle(self, *args, **options):
        test_histories = TestHistory.objects.all()
        test_type_mapping = {
            1: "Practice",
            2: "Mock"
        }

        for test_history in test_histories:
            if test_history.format_name == "None":
                test_history.test_type = 2  # Assign '2' for Mock
            else:
                test_history.test_type = 1  # Assign '1' for Practice

            test_history.save()

            # Output the result with a description
            self.stdout.write(self.style.SUCCESS(
                f'Updated TestHistory ID {test_history.pk} to "{test_type_mapping[test_history.test_type]}"'
            ))
