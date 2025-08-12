from rest_framework import serializers
from .models import Posts

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'title')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'