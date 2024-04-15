from django.core.management.base import BaseCommand
from home.models.test_history import TestHistory
from home.models.question import Question  # Adjust import paths as needed
from home.models.user_test_result import UserTestResult  # Import your UserTestResult model


class Command(BaseCommand):
    help = 'Recalculates scores for all tests based on user answers'

    def handle(self, *args, **options):
        test_histories = TestHistory.objects.all()
        for test_history in test_histories:
            user_score = 0
            total_score = 0
            questions = Question.objects.filter(exam=test_history.exam_name)

            # Check for format filter and apply if exists
            if test_history.format_name is not None:
                try:
                    format_values = list(map(int, test_history.format_name.split(',')))
                    questions = questions.filter(format__in=format_values)
                except ValueError:
                    self.stdout.write(self.style.ERROR(
                        'Error converting format values to integers for TestHistory ID {}'.format(test_history.pk)))
                    continue

            # Recalculate scores
            for question in questions:
                total_score += question.score
                user_test_result = UserTestResult.objects.filter(question_id=question, test_history_id=test_history).first()
                if user_test_result and user_test_result.user_answer == question.correct_option:
                    user_score += question.score  # Increment user_score if answer is correct

            # Update TestHistory with new calculated scores
            test_history.user_score = user_score
            test_history.total_score = total_score
            test_history.save()

            self.stdout.write(self.style.SUCCESS(
                f'Successfully recalculated and updated scores for TestHistory ID {test_history.pk}: Total Score = {total_score}, User Score = {user_score}'))