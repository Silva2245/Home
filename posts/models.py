from django.db import models

# Create your models here.

class Post(models.Model):
    post = models.TextField(null=True, max_length=60000)
