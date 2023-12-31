# Generated by Django 3.2.23 on 2024-01-02 09:01

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='v1704034646/static/images/avatar.b2e01619cc46', max_length=255, verbose_name='image'),
        ),
    ]
