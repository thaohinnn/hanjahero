# Generated by Django 4.2.10 on 2024-04-02 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_user_alter_question_correct_option_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='time_limit',
            field=models.IntegerField(default=1),
        ),
    ]
