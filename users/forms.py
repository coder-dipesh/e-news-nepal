from django import forms
from users.models import *


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
            'placeholder': 'Your Comment',
            'class': 'form-control form-control-user',
        })
