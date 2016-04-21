from __future__ import unicode_literals

from django.db import models

# Create your models here.
class acortar_Url(models.Model):
    Url = models.CharField(max_length=300)
