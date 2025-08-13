from django.db import models
# from authors.models import Author

# Create your models here.
class Book(models.Model):
    author = models.ForeignKey('authors.author', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title