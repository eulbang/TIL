from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20, unique=True)
    borrowed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author}"