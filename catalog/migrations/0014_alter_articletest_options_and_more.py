# Generated by Django 4.2 on 2023-06-04 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_articletest_due_test'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articletest',
            options={'ordering': ['article']},
        ),
        migrations.RenameField(
            model_name='articletest',
            old_name='testdate',
            new_name='test_date',
        ),
    ]