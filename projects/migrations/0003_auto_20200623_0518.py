# Generated by Django 3.0.7 on 2020-06-23 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_asana_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='asana_id',
            field=models.IntegerField(default=None),
        ),
    ]
