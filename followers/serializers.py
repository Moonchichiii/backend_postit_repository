from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Follower
from profiles.models import Profile


User = get_user_model()



class FollowerSerializer(serializers.ModelSerializer):
    followed_profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), write_only=True)    
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Follower
        fields = ['id', 'user', 'followed_profile','user_username']
        extra_kwargs = {
            'user': {'read_only': True},
        }

    def create(self, validated_data):        
        user = self.context['request'].user
        followed_profile = validated_data['followed_profile']
        instance, created = Follower.objects.get_or_create(user=user, followed_profile=followed_profile)
        return instance
        

    def validate(self, data):
        
        user = self.context['request'].user
        followed_profile = data['followed_profile']
        if user == followed_profile.user:
            raise serializers.ValidationError("You cannot follow yourself.")
        if Follower.objects.filter(user=user, followed_profile=followed_profile).exists():
            raise serializers.ValidationError("The user is already following this profile.")
        return data
