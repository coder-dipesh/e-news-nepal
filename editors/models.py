from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from editors.utils import *
from admins.models import Category
# Create your models here.


class NewsModel(models.Model):
    title = models.CharField(max_length=1000)
    category = models.ForeignKey(
        Category, max_length=100, null=True, on_delete=models.CASCADE)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(NewsModel, self).save(*args, **kwargs)
