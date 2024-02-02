from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Profile
from followers.models import Follower  

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    profile_id = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    profile_image = serializers.ImageField(write_only=True, required=False)
    profile_image_url = serializers.SerializerMethodField()  
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    
    def validate_profile_image(self, value):        
        if value.size > 2 * 1024 * 1024:
            raise ValidationError("Image size larger than 2MB!")
        return value
    
    def update(self, instance, validated_data):
        image = validated_data.pop("profile_image", None)
        profile = super().update(instance, validated_data)

        if image:
            profile.profile_image = image
            profile.save()
        return profile
    
    
    def get_profile_image_url(self, obj):
        if obj.profile_image:
            return obj.profile_image.url
        return None 

    def get_profile_id(self, obj):
        request = self.context.get('request')
        user = request.user

        if user.is_authenticated:
            return user.profile.id if hasattr(user, 'profile') else None

        return None

    def get_following_id(self, obj):
        request = self.context.get('request')
        user = request.user

        if user.is_authenticated:
            following_query = Follower.objects.filter(
                profile=user,  
                followed=obj.user  
            )
            if following_query.exists():
                return following_query.first().id
        return None

    class Meta:
        model = Profile
        fields = [
            'user',
            'created_at',
            'updated_at',
            'profile_id',
            'profile_image',  
            'profile_image_url',  
            'following_id',
            'posts_count',
            'followers_count',
            'following_count',
        ]
