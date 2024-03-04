from django.db import models


class QuestionMetaData(models.Model):
    question_meta_id = models.AutoField(primary_key=True)
    question_meta_text = models.TextField()
    level = models.IntegerField()
