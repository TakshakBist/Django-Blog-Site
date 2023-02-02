"""
    Doing this because I don't want to create profiles using admin panel.
    Let's get this over with.
    Don't forget to import it to apps.py in order to apply its effect.
"""

from django.db.models.signals import post_save  # this is the signal that gets fired
from django.contrib.auth.models import User  # this is the sender
from django.dispatch import receiver  # this is the receiver
from .models import Profile

"""
    When sender which is User sends post_save signal, create_profile(receiver) receives it.
    create_profile sends all four arguments passed by post save
    One of the parameter is instance of the user
    So if user is created then create a profile object with user that equals to instance of the user that was created.
    
"""


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

