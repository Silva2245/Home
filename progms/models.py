from django.db import models

# Create your models here.

class Progm(models.Model):
    progm = models.FileField(upload_to='progms', null=True)
