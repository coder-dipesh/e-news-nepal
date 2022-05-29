from users.models import ReportNewsModel
from django import forms


# class ReportNewsForm(forms.ModelForm):
# class Meta:
#     model = ReportNewsModel
#     fields = "__all__"

class ReportNewsForm(forms.ModelForm):
    class Meta:
        model = ReportNewsModel
        fields = ['name', 'email', 'contact', 'category', 'content', 'image']

    # Overriding the form-control

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'name': 'name',
            'id': 'name',
            'placeholder': 'Your Name',
            'class': 'form-control form-control-user',
        })
        self.fields['email'].widget.attrs.update({
            'name': 'email',
            'id': 'email',
            'placeholder': 'Your Email',
            'class': 'form-control form-control-user',
        })
        self.fields['contact'].widget.attrs.update({
            'name': 'contact',
            'id': 'contact',
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
