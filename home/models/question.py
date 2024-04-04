from django.db import models

from home.models.question_meta_data import QuestionMetaData
from home.const.format import format


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.TextField(null=True)
    option_1 = models.TextField(null=True)
    option_2 = models.TextField(null=True)
    option_3 = models.TextField(null=True)
    option_4 = models.TextField(null=True)
    correct_option = models.IntegerField(null=True)
    score = models.IntegerField(default=2)
    exam = models.IntegerField(null=True)
    skill = models.IntegerField(null=True)
    format = models.IntegerField(null=True)
    level = models.IntegerField(null=True)
    question_meta_data = models.ForeignKey(QuestionMetaData, on_delete=models.RESTRICT, blank=True, null=True)
    time_limit = models.IntegerField(default=1)  # Add the time_limit field


