# Generated by Django 3.0 on 2022-04-24 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20220424_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='liked_videos',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='saved_playlists',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='subscribed_channels',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='viewed_videos',
        ),
    ]