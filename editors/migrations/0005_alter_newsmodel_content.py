# Generated by Django 4.0.4 on 2022-05-30 13:09

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('editors', '0004_newsmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='content',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
