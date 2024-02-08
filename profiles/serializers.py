from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    profile_image = serializers.ImageField(write_only=True, required=False)
    profile_image_url = serializers.SerializerMethodField()    
    profile_owner = serializers.SerializerMethodField(method_name='get_is_profile_owner')    
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def validate_profile_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise ValidationError("Image size larger than 2MB!")
        return value

    def update(self, instance, validated_data):
        image = validated_data.pop("profile_image", None)

        if image:
            instance.profile_image = image

        instance.save()
        return instance

    def get_profile_image_url(self, obj):
        if obj.profile_image:
            return obj.profile_image.url
        return None

    def get_is_profile_owner(self, obj):
        request = self.context.get('request', None)
        return obj.user == request.user if request and request.user.is_authenticated else False

    
    class Meta:
        model = Profile
        fields = [
            'user',
            'profile_image',
            'profile_image_url',
            'created_at',
            'updated_at',
            'id', 'user', 
            'profile_owner', 
            'posts_count', 'followers_count', 'following_count',
        ]