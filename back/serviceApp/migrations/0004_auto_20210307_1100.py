# Generated by Django 3.1.5 on 2021-03-07 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceApp', '0003_auto_20210306_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazon',
            name='amazonNumber',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='netflix',
            name='netflixNumber',
            field=models.TextField(blank=True, null=True),
        ),
    ]