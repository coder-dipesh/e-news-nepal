from .models import ReportNewsModel
from django import forms


class ReportNewsForm(forms.ModelForm):
    class Meta:
        model = ReportNewsModel
        fields = ['rname','remail','rcontact', 'rcategory', 'rcontent', 'rimage']

    # Overriding the form-control

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rname'].widget.attrs.update({
            'name': 'rname',
            'id': 'rname',
            'placeholder': 'Your Name',
            'class': 'form-control form-control-user ',
        })
        self.fields['remail'].widget.attrs.update({
            'name': 'remail',
            'id': 'remail',
            'placeholder': 'Your Email',
            'class': 'form-control form-control-user ',
        })
        self.fields['rcontact'].widget.attrs.update({
            'name': 'rcontact',
            'id': 'rcontact',
            'placeholder': 'Your Contact',
            'class': 'form-control form-control-user ',
        })
        self.fields['rcategory'].widget.attrs.update({
            'name': 'rcategory',
            'id': 'rcategory',
            'placeholder': 'Choose Category',
            'class': 'full-width categorycss',
        })
        self.fields['rcontent'].widget.attrs.update({
            'name': 'rcontent',
            'id': 'rcontent',
            'placeholder': 'Write News',
            'class': 'full-width categorycss',
        })
        self.fields['rimage'].widget.attrs.update({
            'name': 'rimage',
            'id': 'rimage',
            'class': 'inputfile inputfile-6 ',
        })
