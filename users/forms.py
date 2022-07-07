from django import forms
from users.models import *
from accounts.models import *
from django.forms import ModelForm




class ReportNewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ['name', 'email', 'contact', 'category', 'content', 'image']

    # Overriding the form-control
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({
            'name': 'category',
            'id': 'category',
            'placeholder': 'Your Comment',
            'class': 'full-width categorycss',
        })
        self.fields['image'].widget.attrs.update({
            'name': 'image',
            'id': 'image',
            'class': 'form-control form-control-user',
        })


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    # Overriding the form-control
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['content'].widget.attrs.update({
            'name': 'content',
            'id': 'content',
            'placeholder': 'Write your comment...',
            'cols': '70',
            'class': 'form-control form-control-user',
        })


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'bio',
                  'phone', 'address', 'city', 'profile_pic']

    # Overriding the form-control
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['profile_pic'].widget.attrs.update({
            'name': 'profile_pic',
            'id': 'profile_pic',
            'class': 'full-width validate',
        })

class contactForm(forms.ModelForm):
    class Meta:
        model = contactinfo
        fields = "__all__"




