from django.db import models
from django.contrib.auth.models import User
from editors.utils import *
from admins.models import Category
from ckeditor.fields import RichTextField
from tinymce import models as tinymce_models


class NewsModel(models.Model):

    status = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )

    title = models.CharField(max_length=1000, null=True)
    category = models.ForeignKey(
        Category, max_length=100, null=True, on_delete=models.CASCADE)
    content = tinymce_models.HTMLField(null=True)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.FileField(upload_to='news/', null=True)
    status = models.CharField(max_length=1, choices=status, default='D')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    like = models.ManyToManyField(User, blank=True, related_name='likes')

    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(NewsModel, self).save(*args, **kwargs)

    def get_date(self):
        return self.modified.date()
