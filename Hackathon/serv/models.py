from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Serv (models.Model):
    ip = models.CharField(max_length=50,primary_key=True)
    rpass = models.CharField(max_length=50,null=True)
    location = models.TextField(blank=True, null=True)
