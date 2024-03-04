from django.db import models

from home.models.question_meta_data import QuestionMetaData
from home.models.test import Test


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.TextField()
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField()
    option_4 = models.TextField()
    correct_option = models.IntegerField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True)
    skill = models.IntegerField(null=True)
    format = models.IntegerField(null=True)
    level = models.IntegerField(null=True)
    question_meta_data = models.ForeignKey(QuestionMetaData, on_delete=models.RESTRICT, blank=True, null=True)
