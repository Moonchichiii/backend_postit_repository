from rest_framework import serializers

from comments.models import Comment
from comments.serializers import CommentSerializer
from likes.models import Like
from likes.serializers import LikeSerializer  
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    profile_username = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},
            "profile": {"read_only": True},
            "image": {"required": False}
        }

    def get_profile_username(self, obj):
        """
        usersname and profile name associated with the post
        """
        return obj.profile.user.username if obj.profile else None

    def validate_post_image(self, value):
        """
        Image validation 
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Image size larger than 2MB!")
        if value.image.height > 4096:
            raise serializers.ValidationError("Image height larger than 4096px")
        if value.image.width > 4096:
            raise serializers.ValidationError("Image width larger than 4096px!")
        return value

    def create(self, validated_data):
        """
        post creation. 
        """
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        updates existing post
        """
        return super().update(instance, validated_data)
    
    def get_comments(self, obj):
        """
        limits the comments returned to 5 based on date. 
        """
        comments = Comment.objects.filter(post=obj).order_by('-created_at')[:5]
        return CommentSerializer(comments, many=True).data