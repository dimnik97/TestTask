# Generated by Django 3.0.7 on 2020-06-23 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='asana_id',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
