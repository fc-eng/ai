# Generated by Django 4.2 on 2023-06-04 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_schoolexam_article_articletest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articletest',
            options={'ordering': ['testdate']},
        ),
    ]
