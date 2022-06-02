from django import forms
from users.models import *


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
