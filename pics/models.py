from django.db import models

# Create your models here.

class Pic(models.Model):
    pic = models.ImageField(upload_to='pics', null=True)
