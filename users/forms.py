from users.models import ReportNewsModel
from django import forms


# class ReportNewsForm(forms.ModelForm):
    # class Meta:
    #     model = ReportNewsModel
    #     fields = "__all__"

class ReportNewsForm(forms.ModelForm):
    class Meta:
        model = ReportNewsModel
        fields = ['name','email','contact', 'category', 'content', 'image']

    # Overriding the form-control

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['category'].widget.attrs.update({
            'name': 'category',
            'id': 'category',
            'placeholder': 'Choose Category',
            'class': 'full-width categorycss',
        })
        self.fields['content'].widget.attrs.update({
            'name': 'content',
            'id': 'content',
            'placeholder': 'Write News',
            'class': 'full-width categorycss',
        })
