from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    