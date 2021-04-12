from python_task.viewsets import song_fileViewset
from rest_framework import routers

router_file = routers.DefaultRouter()
router_file.register('song_file', song_fileViewset)

