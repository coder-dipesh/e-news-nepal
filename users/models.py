from django.db import models
from django.contrib.auth.models import User
from users.utils import *
from editors.models import NewsModel


class Comment(models.Model):
    post = models.ForeignKey(NewsModel, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.post.title, self.user.username)
