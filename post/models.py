from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models

import authuser.models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(authuser.models.User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/posts/' , blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.author}'
