

from statistics import mode
from .models import NewsModel
from django.forms import ModelForm
from django import forms


class NewsForm(forms.ModelForm):

    class Meta:
        model = NewsModel
        fields = '__all__'
