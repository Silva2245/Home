from django.db import models

# Create your models here.

class Song(models.Model):
    song = models.FileField(upload_to='songs', null=True)