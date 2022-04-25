# Generated by Django 3.0 on 2022-04-23 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20200924_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='liked_videos',
            field=models.ManyToManyField(null=True, related_name='user_liked_videos', to='core.Video'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='saved_playlists',
            field=models.ManyToManyField(null=True, to='core.Playlist'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='viewed_videos',
            field=models.ManyToManyField(null=True, related_name='user_viewed_videos', to='core.Video'),
        ),
    ]