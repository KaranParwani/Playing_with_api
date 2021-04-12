from rest_framework import viewsets
from . import models
from . import serializers

class song_fileViewset(viewsets.ModelViewSet):
    queryset = models.song_file.objects.all()
    serializer_class = serializers.song_fileSerializer