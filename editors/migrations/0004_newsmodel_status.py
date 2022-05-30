# Generated by Django 4.0.4 on 2022-05-30 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editors', '0003_newsmodel_contact_newsmodel_email_newsmodel_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], default='D', max_length=1),
        ),
    ]
