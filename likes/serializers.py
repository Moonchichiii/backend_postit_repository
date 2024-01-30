from rest_framework import serializers
from .models import Like
from profiles.models import Profile

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'profile', 'post', 'created_at']
        read_only_fields = ['profile', 'post', 'created_at']

    def create(self, validated_data):        
        return super().create(validated_data)
    
    def get_profile_username(self, obj):
        """
        username with most likes. 
        """
        return obj.profile.user.username if obj.profile else None
