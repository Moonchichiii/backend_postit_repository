from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from profiles.models import Profile


# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_by')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='likes')  
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','profile', 'post')
