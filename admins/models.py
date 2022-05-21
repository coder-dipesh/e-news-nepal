from django.db import models
from django.contrib.auth.models import User
# Create your models here.

editor_role = (("Senior Editor", "Senior Editor"),
               ("Junior Editor", "Junior Editor"),
               ("Assistant Editor", "Assistant Editor"),
               ("Intern Editor", "Intern Editor"))


class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=editor_role)
    salary = models.CharField(max_length=6)

    def __str__(self):
        return self.user.username

# This is the user Category models


class Category(models.Model):
    title = models.CharField(max_length=100)
    categoryName = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.categoryName
