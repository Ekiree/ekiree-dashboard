# Generated by Django 2.1.1 on 2020-04-01 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ed', '0018_edcourse_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvedcourse',
            name='replacement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ed.EDCourse'),
        ),
    ]
