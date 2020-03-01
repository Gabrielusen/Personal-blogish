from django.db import models
from datetime import datetime
from django.urls import reverse     # new


class Post(models.Model):
    text = models.CharField(max_length=250)
    message = models.TextField(max_length=255, default='')
    published = models.DateTimeField("date_published", default=datetime.now())

    def __str__(self):
        return f"{self.text}"

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])  # new
