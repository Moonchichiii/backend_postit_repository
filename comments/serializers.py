from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    profile_username = serializers.ReadOnlyField(source='profile.user.username')

    class Meta:
        model = Comment
        fields = ['id', 'profile', 'profile_username', 'post', 'content', 'created_at']
        read_only_fields = ['profile', 'post', 'created_at', 'profile_username']
