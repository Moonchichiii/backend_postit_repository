from rest_framework import serializers
from cloudinary_storage.storage import MediaCloudinaryStorage
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user", "bio", "profile_image"]

    def validate_profile_image(self, value):
        """
        Validates the size and dimensions of the uploaded image.
        """
        max_size_mb = 1
        max_height_px = 1080
        max_width_px = 1080

        if value.size > max_size_mb * 1024 * 1024:
            raise serializers.ValidationError(
                f"Profile image size larger than {max_size_mb}MB."
            )

        if value.image.height > max_height_px:
            raise serializers.ValidationError(
                f"Profile image height larger than {max_height_px}px"
            )

        if value.image.width > max_width_px:
            raise serializers.ValidationError(
                f"Profile image width larger than {max_width_px}px"
            )

        return value

    def update(self, instance, validated_data):
        image = validated_data.pop("profile_image", None)

        if image:
            storage = MediaCloudinaryStorage()
            profile_image_url = storage.url(storage.save(image.name, image))
            instance.profile_image = profile_image_url

        return super().update(instance, validated_data)
