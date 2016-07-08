from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Serv (models.Model):
    ip = models.GenericIPAddressField()
    location = models.TextField(blank=True, null=True)
