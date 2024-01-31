from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user", "profile_image"]
        extra_kwargs = {
            'user': {'read_only': True},
        }