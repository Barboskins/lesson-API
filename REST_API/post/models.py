from django.db import models

# Create your models here.
class Comment(models.Model):
    author = models.CharField(max_length=50, null=True, blank=True)
    text = models.TextField(null=False, default=None)
