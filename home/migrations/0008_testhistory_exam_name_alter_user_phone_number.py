# Generated by Django 4.2.11 on 2024-04-07 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_question_correct_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='testhistory',
            name='exam_name',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]