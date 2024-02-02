from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile

# Create your models here.


class Follower(models.Model):
    profile = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['profile', 'followed']

    def __str__(self):
        return f'{self.profile.username} follows {self.followed.username}'                                          