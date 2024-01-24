from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from posts.models import Post  

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Post)
def assign_profile_to_post(sender, instance, created, **kwargs):
    if created and hasattr(instance.user, 'profile'):
        instance.profile = instance.user.profile
        instance.save()
