from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.CharField(max_length=1500, blank=False)
    auther = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    comments = models.ManyToManyField(Comment, blank=True, default=None)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:50]