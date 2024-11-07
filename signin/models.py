from django.db import models

# Create your models here.

class Member(models.Model):
    uname = models.CharField(primary_key=True, max_length=55)
    passwd = models.CharField(max_length=100, null=False)
