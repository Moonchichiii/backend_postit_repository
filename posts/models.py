from django.contrib.auth.models import User
from django.db import models
from profiles.models import Profile


class Post(models.Model):
    profile = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)    
    ingredients = models.TextField(blank=True, null=True)
    recipe = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', default='7190932_ugiaz9.png', blank=True)    
    image_url = models.URLField(blank=True) 
    published = models.BooleanField(default=False)
    time = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Post {self.pk}: {self.title}'
