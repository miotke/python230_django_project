from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name='category')


    def __str__(self):
        return self.name
