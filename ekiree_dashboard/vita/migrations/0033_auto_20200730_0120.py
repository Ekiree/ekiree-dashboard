# Generated by Django 2.2.13 on 2020-07-30 08:20

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vita', '0032_auto_20200730_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='offcampusexperience',
            name='essay',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='offcampusexperience',
            name='notes_director',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]
