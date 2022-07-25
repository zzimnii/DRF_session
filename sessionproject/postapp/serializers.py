from rest_framework.serializers import ModelSerializer
from .models import Post, Comment
from rest_framework import serializers


class PostSerializer(ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Post
        fields = ['id', 'title', 'photo', 'user' ]


class CommentSerializer(ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    class Meta:
        model = Comment
        fields = [ 'id', 'post', 'comment', 'user' ]