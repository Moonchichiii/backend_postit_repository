from rest_framework import serializers
from .models import Post
from cloudinary_storage.storage import MediaCloudinaryStorage

class PostSerializer(serializers.ModelSerializer):
    post_image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def validate_post_image(self, value):
        """
        Validates the size and dimensions of the uploaded image.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError('Image height larger than 4096px')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width larger than 4096px!')
        return value

    def create(self, validated_data):
        image = validated_data.pop('post_image', None)

        post = super().create(validated_data)

        if image:
            self.save_image(post, image)

        return post

    def update(self, instance, validated_data):
        image = validated_data.pop('post_image', None)

        post = super().update(instance, validated_data)

        if image:
            self.save_image(post, image)

        return post

    def save_image(self, instance, image):
        """
        Uploads the image and saves the image URL to the specified image field.
        """
        storage = MediaCloudinaryStorage()
        image_url = storage.save(image.name, image)
        instance.image = image_url 
        instance.save()
