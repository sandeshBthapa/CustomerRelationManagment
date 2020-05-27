from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from .models import Customer


def create_profile(sender, created, instance, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(user=instance, name=instance.username)


post_save.connect(create_profile, sender=User)
