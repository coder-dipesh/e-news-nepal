from django.db import models
from django.contrib.auth.models import User
from users.utils import *
from admins.models import Category
from ckeditor.fields import RichTextField


# Create your models here.


class ReportNewsModel(models.Model):
    rname = models.CharField(max_length=1000)
    remail = models.CharField(max_length=1000)
    rcontact = models.CharField(max_length=1000)
    rcategory = models.ForeignKey(
        Category, max_length=100, null=True, on_delete=models.CASCADE)
    rcontent = RichTextField(blank=True, null=True)
    rslug = models.SlugField(max_length=1000, null=True, blank=True)
    ruser = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    rimage = models.FileField(upload_to='news/')
    rcreated_at = models.DateTimeField(auto_now_add=True)
    rupload_to = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.modified = None

    def __str__(self):
        return self.rname

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.rname)
        super(ReportNewsModel, self).save(*args, **kwargs)

    def get_date(self):
        return self.modified.date()
