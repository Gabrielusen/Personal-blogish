from django.db import models
from datetime import datetime, timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.title}"
