from django.db import models

class Posts(models.Model):
    title = models.CharField()
    content = models.TextField()