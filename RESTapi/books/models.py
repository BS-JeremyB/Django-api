from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    publication_date = models.DateField()
    genre = models.CharField(max_length=50)
    note = models.FloatField(default=0)
    owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)

    