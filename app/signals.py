from django.db.models.signals import post_save,post_delete, pre_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile


# Signal function to create a profile when a user is created
@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Signal function to delete user when related profile is deleted
@receiver(post_delete, sender=Profile)
def post_delete_user(sender, instance, **kwargs):
    # Delete user when related profile is deleted.
    instance.user.delete()