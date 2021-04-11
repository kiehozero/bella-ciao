from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """ User profile for storing order history,
    account information and loyalty points """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # all options as users aren't obliged to store this information
    default_name = models.CharField(max_length=50, null=True, blank=True)
    default_phone_number = models.CharField(
        max_length=15, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_city = models.CharField(max_length=20, null=True, blank=True)
    default_eircode = models.CharField(max_length=7, null=True, blank=True)


    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """ Create profile if a new user or
    update profile if an existing user"""

    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
