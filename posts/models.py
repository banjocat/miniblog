from __future__ import unicode_literals
from django.utils import timezone

from django.db import models

POST_STATUS = (
    (1, 'DRAFT'),
    (2, 'POSTED'),
    (3, 'DELETED')
)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30, default='')
    author = models.CharField(max_length=50, default='Jack')
    text = models.TextField(default='')
    publish_date = models.DateField(default=timezone.now)
    tags = models.ManyToManyField('Tag')
    status = models.IntegerField(choices=POST_STATUS)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
