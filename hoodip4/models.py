from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profiles/')

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


    def __str__(self):
        return self.user_name

