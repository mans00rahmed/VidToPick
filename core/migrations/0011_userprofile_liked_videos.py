# Generated by Django 3.0.8 on 2020-09-14 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_video_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='liked_videos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Video'),
        ),
    ]
