from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from accounts.models import Profile

from django.core.exceptions import ValidationError


import re
EMAIL_REGEX = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"


class CreateUserForm(UserCreationForm):

    # Overriding usercreatiion form to design signup page
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'required': '',
            'name': 'first_name',
            'id': 'first_name',
            'type': 'text',
            'class': 'form-control form-control-user',
            'placeholder': 'First Name',
            'maxlength': '16',
            'minlength': '6',
        })
        self.fields['last_name'].widget.attrs.update({
            'required': '',
            'name': 'last_name',
            'id': 'last_name',
            'type': 'text',
            'class': 'form-control form-control-user',
            'placeholder': 'Last Name',
            'maxlength': '16',
            'minlength': '6',
        })

        self.fields['username'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'class': 'form-control form-control-user',
            'placeholder': 'Username',
            'maxlength': '16',
            'minlength': '6',
        })
        self.fields['email'].widget.attrs.update({
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'class': 'form-control form-control-user',
            'placeholder': 'you@example.com',

        })

        self.fields['password1'].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'class': 'form-control form-control-user',
            'placeholder': '********',
            'maxlength': '22',
            'minlength': '8',
        })
        self.fields['password2'].widget.attrs.update({
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'class': 'form-control form-control-user',
            'placeholder': '********',
            'maxlength': '22',
            'minlength': '8',
        })

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")

        if not re.search(EMAIL_REGEX, email):
            print("Invalid Email ")
            raise forms.ValidationError("Invalid Email Address")

        return email

        return email


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'bio',
                  'phone', 'address', 'city', 'profile_pic']

        widgets = {
            'profile_pic': forms.FileInput(attrs={'class': 'form-control validate'}),
        }
