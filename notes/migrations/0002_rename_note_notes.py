# Generated by Django 4.1.3 on 2022-11-28 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Note',
            new_name='Notes',
        ),
    ]
