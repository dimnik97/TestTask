# Generated by Django 3.0.7 on 2020-06-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='asana_id',
            field=models.CharField(default=None, max_length=40),
        ),
    ]
