from .models import NewsModel
from django import forms
from froala_editor.widgets import FroalaEditor


class NewsForm(forms.ModelForm):
    content = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = NewsModel
        fields = ['title', 'category', 'content', 'image']

    # Overriding the form-control

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'required': '',
            'name': 'title',
            'id': 'title',
            'placeholder': 'Your News Title',
            'class': 'form-control form-control-user',
        })
        self.fields['category'].widget.attrs.update({
            'required': '',
            'name': 'category',
            'id': 'category',
            'placeholder': 'Choose Category',
            'class': 'form-control form-control-user',
        })
        self.fields['image'].widget.attrs.update({
            'required': '',
            'name': 'image',
            'id': 'image',
            'class': 'form-control form-control-user',
        })
        self.fields['content'].widget.attrs.update({
            'required': '',
            'name': 'content',
            'id': 'content',
            'class': 'form-control form-control-user',
        })
