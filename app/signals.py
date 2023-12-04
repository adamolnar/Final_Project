from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile


# Signal function to create a profile when a user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)