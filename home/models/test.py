from django.db import models


class Test(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=50)
    level = models.IntegerField()
