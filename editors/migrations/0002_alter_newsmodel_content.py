# Generated by Django 4.0.4 on 2022-05-25 11:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]