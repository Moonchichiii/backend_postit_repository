from django.contrib.auth.models import User
from django.db import models
from profiles.models import Profile

  
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', default='7190932_ugiaz9.png', blank=True)
    published = models.BooleanField(default=True)
    time = models.IntegerField(default=0)  

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        
        return f'Post {self.id}: {self.title}'