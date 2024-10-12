from django.db import models

# Create your models here.

class v(models.Model):
    uname = models.CharField(max_length=255, null=True)
    passwd = models.CharField(max_length=255, null=True)
