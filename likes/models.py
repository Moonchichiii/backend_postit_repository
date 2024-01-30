from django.db import models
from posts.models import Post
from profiles.models import Profile

class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('profile', 'post')

    def __str__(self):
        return f"Like by {self.profile.user.username} post ID {self.post.id}"




