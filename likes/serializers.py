from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'profile', 'post', 'created_at']
        read_only_fields = ['profile', 'post', 'created_at']

    def create(self, validated_data):        
        return super().create(validated_data)
    
    
    