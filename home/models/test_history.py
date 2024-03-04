from django.db import models

from home.models.question import Test
from home.models.user import User


class TestHistory(models.Model):
    test_history_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    test_date = models.DateField()
    score = models.FloatField()
