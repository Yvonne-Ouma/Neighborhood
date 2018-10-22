from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Neighborhood(models.Model):
    range = (
        ('Nairobi', 'Nairobi'),
        ('kisumu', 'kisumu'),
        ('Ayany', 'Ayany'),
        ('Fort_Jesus', 'Fort_Jesus'),
        ('Kampala', 'Kampala'),

    )

    neighborhood_location = models.CharField(choices=range, max_length=200 ,default=0, null=True, blank=True)
    name = models.CharField(max_length=30)
    population= models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

    def save_neighborhood(self):
        self.save()

    @classmethod
    def delete_neighborhood_by_id(cls, id):
        neighbourhoods = cls.objects.filter(pk=id)
        neighbourhoods.delete()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

class Location(models.Model):
    choice_field = (
        ('Nairobi', 'Nairobi'),
        ('kisumu', 'kisumu'),
        ('Ayany', 'Ayany'),
        ('Fort_Jesus', 'Fort_Jesus'),
        ('Kampala', 'Kampala'),

    )
    name = models.CharField(choices=choice_field, max_length=200 , blank=True)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profiles/')
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, blank=True, null=True)
    location = models.ForeignKey(Location, null=True, blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


    def __str__(self):
        return self.user_name


class Posts(models.Model):
    
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='picture/', )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="posts")
    description = models.TextField()
    location = models.ForeignKey(Location, null=True, blank=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def delete_image_by_id(cls, id):
        pictures = cls.objects.filter(pk=id)
        pictures.delete()

    # @classmethod
    # def get_image_by_id(cls, id):
    #     pictures = cls.objects.get(pk=id)
    #     return pictures

    # @classmethod
    # def filter_by_location(cls, location):
    #     pictures = cls.objects.filter(location=location)
    #     return pictures

    # @classmethod
    # def search_image(cls, search_term):
    #     pictures = cls.objects.filter(name__icontains=search_term)
    #     return pictures

    # @classmethod
    # def update_image(cls, id):
    #     pictures = cls.objects.filter(id=id).update(id=id)
    #     return pictures

    # @classmethod
    # def update_description(cls, id):
    #     pictures = cls.objects.filter(id=id).update(id=id)
    #     return pictures 

class Business(models.Model):
    business_name = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="images")
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, blank=True, null=True)
    business_email = models.CharField(max_length=40)
    
    def __str__(self):
        return self.business_name

    def save_business(self):
        self.save()

    @classmethod
    def filter_by_search_term(cls, search_term):
        return cls.objects.filter(business_name__icontains=search_term)    

