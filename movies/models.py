from django.db import models

# Create your models here.

class Movie(models.Model):
    movie = models.FileField(upload_to='movies', null=True)
