# Generated by Django 4.2 on 2023-06-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_rename_answer_articletest_reply_articletest_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletest',
            name='due_test',
            field=models.DateField(blank=True, null=True),
        ),
    ]
