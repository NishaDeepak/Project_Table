# Generated by Django 3.1.1 on 2020-10-10 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201010_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='access_records',
            old_name='Date',
            new_name='date',
        ),
    ]
