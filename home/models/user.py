from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20, null=True)
    username = models.EmailField(unique=True)
    time_created = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=255)
