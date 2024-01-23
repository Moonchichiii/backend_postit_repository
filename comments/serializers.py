from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'profile', 'post', 'content', 'created_at']
        read_only_fields = ['profile','title', 'post', 'created_at' ]
        