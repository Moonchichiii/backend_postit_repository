from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile

class Follower(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'followed_profile'),)

    def __str__(self):
        return f'{self.user.username} follows {self.followed_profile.user.username}'
