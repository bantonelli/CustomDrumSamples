from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    last_4_digits = models.CharField(max_length=4, blank=True)
    stripe_id = models.CharField(max_length=255, blank=True)
    subscribed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
User.get_or_create_profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

"""
We are defining a new property for the User model.
    The new property is called profile.
    Whenever you pass in a User object to this property it will get or create a UserProfile for this user.
    When we access the User object's profile property this code will get triggered and create a UserProfile that
    is linked to the User object.
"""

# Access a User's profile by doing --> user_instance.profile
# Any changes made to it have to be saved
# use this to save--> user_instance.profile.save() method

from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver


@receiver(post_save, sender=User)
def user_save(sender, instance, **kwargs):
    instance.get_or_create_profile

