from django.db import models

class Posts(models.Model):
    title = models.CharField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)