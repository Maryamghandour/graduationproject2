# Generated by Django 4.0.3 on 2022-04-16 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='index',
        ),
    ]
