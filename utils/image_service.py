from rest_framework import serializers

class ImageValidation:
    def validate_image(self, value):
        """
        Validates the size and dimensions of the uploaded image.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError('Image height larger than 4096px!')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width larger than 4096px!')
        return value

    def save_image(self, instance, image_field_name, image):
        """
        Uploads the image and saves the image URL to the specified image field.
        """
        if image:
            image_url = upload_image(image)
            setattr(instance, image_field_name, image_url)
            instance.save()
            return instance