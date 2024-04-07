from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20, null=True)
    email_address = models.EmailField(unique=True)
    time_created = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=20)