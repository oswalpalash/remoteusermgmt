from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users (models.Model):
    userid = models.CharField(max_length=50,primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
