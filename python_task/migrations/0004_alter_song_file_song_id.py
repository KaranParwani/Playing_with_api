# Generated by Django 4.0.dev20210219192511 on 2021-04-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_task', '0003_song_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song_file',
            name='song_id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]