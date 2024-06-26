from django.db import models

from home.models.user import User


class TestHistory(models.Model):
    test_history_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_name = models.IntegerField(default=0)
    skill_name = models.IntegerField(default=0)
    format_name = models.JSONField(null=True)
    test_date = models.DateField()
    user_score = models.IntegerField()
    total_score = models.IntegerField()
    time_limit = models.IntegerField(default=0)
    format_statistics = models.JSONField(null=True)
    test_type = models.IntegerField(default=0)
    level = models.IntegerField(null=True)
