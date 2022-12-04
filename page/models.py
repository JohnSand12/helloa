from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=400)
    password = models.CharField(max_length=400)