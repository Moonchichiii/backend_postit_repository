from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField('image', default='default_pfp_ivf3fa')

    def __str__(self):
        return f'{self.user.username} Profile'
