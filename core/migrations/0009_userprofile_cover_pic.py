# Generated by Django 3.0.8 on 2020-09-12 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_video_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cover_pic',
            field=models.ImageField(default='coverpic/default.jpg', null=True, upload_to='coverpic/'),
        ),
    ]
