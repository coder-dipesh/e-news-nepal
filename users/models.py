from django.db import models
from django.contrib.auth.models import User
from users.utils import *
from admins.models import Category
from ckeditor.fields import RichTextField
# Create your models here.


class ReportNewsModel(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    contact = models.CharField(max_length=1000)
    category = models.ForeignKey(
        Category, max_length=100, null=True, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    image = models.FileField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.name)
        super(ReportNewsModel, self).save(*args, **kwargs)

    def get_date(self):
        return self.modified.date()
