"""
    Django ORM is good but not as good as Spring Boot's ORM.
    Models are the interface that will help us modify/create database tables.
    Classes Created here will be the database tables and the attributes will be columns for our database tables.
    Django has created separate table for user, so we need to import user and use it as foreign key.

"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # if user deletes the account , the post gets deleted

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        # return the reverse of the url
        return reverse('blog-detail', kwargs={'pk': self.pk})

