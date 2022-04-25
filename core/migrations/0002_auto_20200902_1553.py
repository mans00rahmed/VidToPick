# Generated by Django 3.0.8 on 2020-09-02 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='thumbnails/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='video',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commented_date', models.DateTimeField(auto_now=True)),
                ('comment_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.UserProfile')),
                ('commented_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Video')),
            ],
        ),
    ]
