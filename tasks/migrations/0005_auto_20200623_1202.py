# Generated by Django 3.0.7 on 2020-06-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='asana_id',
            field=models.CharField(blank=True, default=None, max_length=40),
        ),
    ]
