# Generated by Django 3.0.3 on 2020-02-04 07:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_votes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='votes',
            new_name='Vote',
        ),
    ]
