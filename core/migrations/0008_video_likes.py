# Generated by Django 3.0.8 on 2020-09-03 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200902_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]