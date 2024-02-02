from rest_framework import serializers
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    profile_username = serializers.ReadOnlyField(source='profile.username')
    followed_username = serializers.ReadOnlyField(source='followed.username')
    class Meta:
        model = Follower
        fields = ['id', 'profile', 'followed', 'created_at', 'profile_username', 'followed_username']