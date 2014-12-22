from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    last_4_digits = models.CharField(max_length=4)
    stripe_id = models.CharField(max_length=255)
    subscribed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

"""
We are defining a new property for the User model.
    The new property is called profile.
    Whenever you pass in a User object to this property it will get or create a UserProfile for this user.
    When we access the User object's profile property this code will get triggered and create a UserProfile that
    is linked to the User object.
"""