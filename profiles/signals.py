from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    creating a profile when a new user is created or updated
    """
    if created:
        
        if not hasattr(instance, 'profile'):
            Profile.objects.create(user=instance)
    else:
        
        if hasattr(instance, 'profile'):
            instance.profile.save()