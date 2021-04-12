
from .models import Post, song_file
from django import forms
from rest_framework  import serializers
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         feild = {
#             'title', 'description'
#         }

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 'description'
        ) 
        
class song_fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = song_file
        fields = '__all__'        