# Generated by Django 4.2.11 on 2024-04-13 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_testhistory_time_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='testhistory',
            name='format_statistics',
            field=models.JSONField(null=True),
        ),
    ]