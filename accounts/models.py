from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100, null=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    bio = models.TextField(max_length=500, blank=True)
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=300, null=True)
    city = models.CharField(max_length=100, null=True)
    profile_pic = models.FileField(
        upload_to='images/', default='images/user.png')

    # Social Links
    facebook = models.CharField(max_length=150, default="#", null=True)
    instagram = models.CharField(max_length=150, default="#", null=True)
    linkedin = models.CharField(max_length=150, default="#", null=True)

    created_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username


class UserOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_st = models.DateTimeField(auto_now=True)
    otp = models.IntegerField()
