from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Article(models.Model):
    # id는 자동으로 만들어진다.
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)