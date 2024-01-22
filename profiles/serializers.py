from django.db import models
from django.contrib.auth import get_user_model
from rest_framework import serializers

from utils.image_service import ImageValidation

from .models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'profile_image']

    def update(self, instance, validated_data):
        image = validated_data.pop('profile_image', None)
        if image:
            image_validator = ImageValidation()
            image_validator.validate_image(image)
            image_validator.save_image(instance, 'profile_image', image)
        return super().update(instance, validated_data)
