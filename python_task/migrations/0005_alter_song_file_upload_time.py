# Generated by Django 4.0.dev20210219192511 on 2021-04-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_task', '0004_alter_song_file_song_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song_file',
            name='upload_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
