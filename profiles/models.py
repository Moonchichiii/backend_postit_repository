from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)   
    profile_image = models.URLField(default='7190932_ugiaz9.png')

    def __str__(self):
        return f'{self.user.username} Profile'
