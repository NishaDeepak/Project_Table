# Generated by Django 3.1.1 on 2020-10-09 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201010_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='Url',
            field=models.URLField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
