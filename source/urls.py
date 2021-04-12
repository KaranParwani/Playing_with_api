"""source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from python_task.views import song_fileView, song_fileUpdate, song_fileDestroy
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .router import router_file

urlpatterns = [
    # path('/', include('python_task.urls')),
    path('', song_fileView.as_view(), name='test'),
    path('delete/<str:pk>', song_fileDestroy.as_view(), name='delete'),
    path('update/<str:pk>', song_fileUpdate.as_view(), name='update'),
    path('admin/', admin.site.urls),
    path('api/', include(router_file.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 