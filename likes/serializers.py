from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    profile_username = serializers.ReadOnlyField(source='profile.user.username')  

    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'profile', 'profile_username', 'created_at']  
        read_only_fields = ['user', 'post', 'created_at', 'profile', 'profile_username']  