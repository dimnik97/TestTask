from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asana_id = models.CharField(default=None, max_length=40)
    name = models.CharField(default=None, max_length=40)
