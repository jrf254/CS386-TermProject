from django.db import models
from django.contrib.auth.models import Group, User, UserManager
from dynamic_forms.models import *
from taggit.managers import TaggableManager
from datetime import datetime, timedelta
# Create your models here.

class project(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    members = TaggableManager()
    enddate = models.DateTimeField(default=datetime.now()+timedelta(days=14))

    def __str__(self):
        return self.name

#     description = models.TextField(max_length=200)
#     email = models.EmailField()
#     username = models.CharField(max_length=30)
#     datetime = models.DateTimeField(auto_now_add=True)
