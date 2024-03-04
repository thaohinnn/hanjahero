from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    phone_number = models.IntegerField()
    email_address = models.EmailField(unique=True)
    time_created = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=20)

class Level(models.Model):
    level_id = models.AutoField(primary_key=True)
    level_name = models.CharField(max_length=10)

class Skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=20)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)



class Format(models.Model):
    format_id = models.AutoField(primary_key=True)
    format_name = models.TextField()

class QuestionMetaData(models.Model):
    question_meta_id = models.AutoField(primary_key=True)
    question_meta_text = models.TextField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

class Test(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=50)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.TextField()
    option_1 = models.TextField()
    option_2 = models.TextField()
    option_3 = models.TextField()
    option_4 = models.TextField()
    correct_option = models.IntegerField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    format = models.ForeignKey(Format, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    question_meta_data = models.ForeignKey(QuestionMetaData, on_delete=models.SET_NULL, blank=True, null=True)

class TestHistory(models.Model):
    test_history_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    test_date = models.DateField()
    score = models.FloatField()
