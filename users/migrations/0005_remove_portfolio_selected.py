# Generated by Django 3.0.8 on 2020-09-21 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='selected',
        ),
    ]
