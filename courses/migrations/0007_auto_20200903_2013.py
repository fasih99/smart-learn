# Generated by Django 2.2.8 on 2020-09-03 20:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_course_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
