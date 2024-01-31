from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_image = models.ImageField(upload_to='profiles/', default='Defaultprofile.png')    
    def __str__(self):
        return f"{self.user.username} Profile"
