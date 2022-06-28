from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Category, CustomUser, Site

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


class CustomUserForm(forms.ModelForm):
    # Overriding usercreatiion form to design signup page
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].widget.attrs.update({
            'required': '',
            'name': 'role',
            'id': 'role',
            'class': 'form-control form-control-user',
        })
        self.fields['salary'].widget.attrs.update({
            'required': '',
            'name': 'salary',
            'id': 'salary',
            'class': 'form-control form-control-user',
            'placeholder': 'Rs.45,000',
        })

    class Meta:
        model = CustomUser
        fields = ['role', 'salary']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'categoryName', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'required': '',
            'name': 'title',
            'id': 'title',
            'class': 'form-control validate',
        })
        self.fields['categoryName'].widget.attrs.update({
            'required': '',
            'name': 'categoryName',
            'id': 'categoryName',
            'class': 'form-control validate',
        })
        self.fields['description'].widget.attrs.update({
            'required': '',
            'name': 'description',
            'id': 'description',
            'class': 'form-control validate',
        })


# This is the custom site setting and about us page form
class SiteSetting(ModelForm):
    class Meta:
        model = Site
        fields = ['title', 'metaDesc', 'metaKey', 'logo', 'favicon', 'aboutimg', 'abouttitle','aboutdesc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'name': 'title',
            'id': 'title',
            'class': 'form-control validate',
        })
        self.fields['metaDesc'].widget.attrs.update({
           
            'name': 'metaDesc',
            'id': 'title',
            'class': 'form-control validate',
        })
        self.fields['metaKey'].widget.attrs.update({
            
            'name': 'metaKey',
            'id': 'title',
            'class': 'form-control validate',
        })
        self.fields['logo'].widget.attrs.update({
            'name': 'logo',
            'type': 'file',
            'id': 'logo',
            'class': 'form-control form-control-user',
        })
        self.fields['favicon'].widget.attrs.update({
            'name': 'favicon',
            'type': 'file',
            'id': 'favicon',
            'class': 'form-control form-control-user',
        })
        self.fields['aboutimg'].widget.attrs.update({
            'name': 'aboutimg',
            'type': 'file',
            'id': 'aboutimg',
            'class': 'form-control form-control-user',
        })
        self.fields['abouttitle'].widget.attrs.update({
            'name': 'abouttitle',
            'id': 'title',
            'class': 'form-control validate',
        })
        self.fields['aboutdesc'].widget.attrs.update({
            'name': 'aboutdesc',
            'id': 'description',
            'class': 'form-control validate',
        })
        
# This is the custom site setting and about us page form
# class SiteSetting(forms.ModelForm):
#     class Meta:
#         model = Site
#         fields = "__all__"
        
