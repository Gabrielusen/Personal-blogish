from django.db import models
#   from datetime import datetime


class Post(models.Model):
    text = models.CharField(max_length=250)
    message = models.TextField(max_length=255, default='')

    def __str__(self):
        return f"{self.text}"
