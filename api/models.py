from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50, default="")
    subtitle = models.CharField(max_length=100, default="")
    content = models.TextField(default="")
    theme = models.CharField(max_length=50, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
