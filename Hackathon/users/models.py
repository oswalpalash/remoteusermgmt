from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users (models.Model):
    username = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)
    projid = models.CharField(max_length=50,default=0) 
