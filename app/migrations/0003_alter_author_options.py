# Generated by Django 3.2.23 on 2023-11-22 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20231121_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['user']},
        ),
    ]