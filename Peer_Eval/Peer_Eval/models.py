from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.

class survey(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    datetime = models.DateTimeField(auto_now_add=True)
