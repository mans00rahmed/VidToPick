# Generated by Django 3.0.8 on 2020-09-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200914_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='liker',
        ),
        migrations.AddField(
            model_name='video',
            name='liker',
            field=models.ManyToManyField(null=True, to='core.UserProfile'),
        ),
    ]
