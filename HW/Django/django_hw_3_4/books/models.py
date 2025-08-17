from django.db import models
from authors.models import Author

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return self.title
    
class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre