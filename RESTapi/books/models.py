from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    publication_date = models.DateField()
    genre = models.CharField(max_length=50)
    note = models.FloatField(default=0)
    