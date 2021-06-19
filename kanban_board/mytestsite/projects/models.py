from django.db import models

# Create your models here.
class Album1(models.Model):
    title = models.TextField()
    genere = models.TextField()
    band = models.TextField()

class Artist(models.Model):
    name = models.TextField()
    sex = models.TextField()

class Nomi(models.Model):
    name = models.TextField()


