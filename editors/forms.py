from .models import NewsModel
from django import forms


class NewsForm(forms.ModelForm):

    class Meta:
        model = NewsModel
        fields = ['title', 'category', 'content', 'image']

    # Overriding the form-control

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'name': 'title',
            'id': 'title',
            'placeholder': 'Your News Title',
            'class': 'form-control form-control-user',
        })
        self.fields['category'].widget.attrs.update({
            'name': 'category',
            'id': 'category',
            'placeholder': 'Choose Category',
            'class': 'form-control form-control-user',
        })
        self.fields['image'].widget.attrs.update({
            'name': 'image',
            'id': 'image',
            'class': 'form-control form-control-user',
        })


class RequestNewsUpdateForm(forms.ModelForm):

    class Meta:
        model = NewsModel
        fields = ['title', 'category', 'content',
                  'image', 'name', 'email', 'contact']

    # Overriding the form-control

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'name': 'title',
            'id': 'title',
            'placeholder': 'Your News Title',
            'class': 'form-control form-control-user',
        })
        self.fields['category'].widget.attrs.update({
            'name': 'category',
            'id': 'category',
            'placeholder': 'Choose Category',
            'class': 'form-control form-control-user',
        })
        self.fields['image'].widget.attrs.update({
            'name': 'image',
            'id': 'image',
            'class': 'form-control form-control-user',
        })
        self.fields['name'].widget.attrs.update({
            'name': 'name',
            'id': 'name',
            'class': 'form-control form-control-user',
        })
        self.fields['email'].widget.attrs.update({
            'name': 'email',
            'id': 'email',
            'class': 'form-control form-control-user',
        })
        self.fields['contact'].widget.attrs.update({
            'name': 'contact',
            'id': 'contact',
            'class': 'form-control form-control-user',
        })
