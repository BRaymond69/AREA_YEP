# Generated by Django 3.1.5 on 2021-03-07 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceApp', '0007_auto_20210307_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amazon',
            name='amazonNumber',
        ),
        migrations.RemoveField(
            model_name='netflix',
            name='netflixNumber',
        ),
    ]
