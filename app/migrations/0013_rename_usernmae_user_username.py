# Generated by Django 3.2.23 on 2023-12-14 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20231214_0841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='usernmae',
            new_name='username',
        ),
    ]