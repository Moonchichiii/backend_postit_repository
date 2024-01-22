from rest_framework import serializers
from utils.image_service import ImageValidation
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    post_image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('post_image', None)
        image_validator = ImageValidation()
        
        if image:
            image_validator.validate_image(image)

        post = super().create(validated_data)

        if image:
            image_validator.save_image(post, 'post_image', image)

        return post

    def update(self, instance, validated_data):
        image = validated_data.pop('post_image', None)
        image_validator = ImageValidation()

        if image:
            image_validator.validate_image(image)
            image_validator.save_image(instance, 'post_image', image)

        return super().update(instance, validated_data)