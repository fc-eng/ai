# Generated by Django 4.2 on 2023-04-19 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_schoolexam_quarter'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolexam',
            name='article',
            field=models.ForeignKey(help_text='원본입력', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.article'),
        ),
    ]