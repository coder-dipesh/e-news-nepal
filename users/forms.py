from users.models import ReportNewsModel
from django import forms


# class ReportNewsForm(forms.ModelForm):
    # class Meta:
    #     model = ReportNewsModel
    #     fields = "__all__"

class ReportNewsForm(forms.ModelForm):
    class Meta:
        model = ReportNewsModel
        fields = ['rname','remail','rcontact', 'rcategory', 'rcontent', 'rimage']

    # Overriding the form-control

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


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
