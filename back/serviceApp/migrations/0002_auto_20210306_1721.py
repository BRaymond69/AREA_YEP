# Generated by Django 3.1.5 on 2021-03-06 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='NewsPapper',
            new_name='newsPapper',
        ),
        migrations.RemoveField(
            model_name='intra',
            name='mail',
        ),
    ]
