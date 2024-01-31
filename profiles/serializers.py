from rest_framework import serializers
from .models import Profile
from followers.models import Follower  

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    profile_id = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()


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
            following = Follower.objects.filter(
                profile=user.profile,
                followed=obj.user
            ).first()
            return following.id if following else None

        return None

    class Meta:
        model = Profile
        fields = [
            'user',
            'created_at',
            'updated_at',
            'profile_id',
            'profile_image',            
            'updated_at',
        ]