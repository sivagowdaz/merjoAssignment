from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    content = models.CharField(max_length=500, blank=False)
    auther = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.auther.username}:{self.content[:10]}"