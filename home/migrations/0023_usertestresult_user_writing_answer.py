# Generated by Django 4.2.11 on 2024-04-29 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_testhistory_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertestresult',
            name='user_writing_answer',
            field=models.TextField(null=True),
        ),
    ]
