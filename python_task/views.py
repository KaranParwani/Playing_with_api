from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer, song_fileSerializer
from rest_framework import generics
from rest_framework import mixins


from .models import Post, song_file
# Create your views here.

class song_fileView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
  
  queryset = song_file.objects.all()
  serializer_class = song_fileSerializer
  
  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)
  
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
  
class song_fileUpdate(mixins.UpdateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
  
  queryset = song_file.objects.all()
  serializer_class = song_fileSerializer
  
  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)
  
  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)    

class song_fileDestroy(mixins.UpdateModelMixin, mixins.ListModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):

  queryset = song_file.objects.all()
  serializer_class = song_fileSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)
  
  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)


# class TestView(APIView):
#     def get(self, request, *args, **kwargs):
#       queryset = Post.objects.all()
#       serializer = PostSerializer(queryset, many=True)
#       return Response(serializer.data)  
    
#     def post(self, request, *args, **kwargs):
#       serializer = PostSerializer(data = request.data)
#       if serializer.is_valid():
#          serializer.save() 
#          return Response(serializer.data)
#       return Response(serializer.errors) 


