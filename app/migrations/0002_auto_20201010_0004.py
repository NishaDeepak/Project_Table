# Generated by Django 3.1.1 on 2020-10-09 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='access_records',
            old_name='Name',
            new_name='name',
        ),
    ]
