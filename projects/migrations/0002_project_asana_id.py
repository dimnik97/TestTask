# Generated by Django 3.0.7 on 2020-06-23 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='asana_id',
            field=models.IntegerField(),
        ),
    ]
