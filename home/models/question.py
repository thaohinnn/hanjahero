from django.db import models


# Create your models here.

class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    question_text = models.TextField()

    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField()
    option_4 = models.TextField()

    correct_option = models.IntegerField()

    # test_id = models.ForeignKey()
    # skill_id = models.ForeignKey()
    # format_id = models.ForeignKey()
    # level_id = models.ForeignKey()
    # question_meta_id = models.ForeignKey()
