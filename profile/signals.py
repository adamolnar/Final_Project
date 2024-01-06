from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


# Signal handler to create a profile when a user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Signal handler to save a profile when a user is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Signal handler to delete user when related profile is deleted
@receiver(post_delete, sender=Profile)
def post_delete_user(sender, instance, **kwargs):
    # Delete user when related profile is deleted.
    instance.user.delete()

