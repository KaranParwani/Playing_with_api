from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
# import mutagen
from django.core.files.uploadedfile import UploadedFile
# from audiofield.fields import AudioField
# Create your models here.

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
class song_file(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=100, null=False)
    song_upload = models.FileField(upload_to = "media")
    duration_seconds = models.PositiveIntegerField("Track duration ins seconds", null=False)
    upload_time = models.DateTimeField(default=datetime.now(), null= False)
    
    def __str__(self):
        return self.song_name
    
  