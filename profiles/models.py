from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)
    profile_image = models.URLField(default="Default_pfp.svg_zssa2m.png")

    def __str__(self):
        return f"{self.user.username} Profile"
