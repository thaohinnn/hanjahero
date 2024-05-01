from django.db import models

from home.models.question import Question
from home.models.test_history import TestHistory


class UserTestResult(models.Model):
    finished_ques_id = models.AutoField(primary_key=True)
    user_answer = models.IntegerField(null=True)
    question_id = models.ForeignKey(Question, on_delete=models.RESTRICT)
    test_history_id = models.ForeignKey(TestHistory, on_delete=models.RESTRICT)
    user_writing_answer = models.TextField(null=True, max_length=1000)
