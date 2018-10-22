from django.contrib import admin
from .models import Profile,Posts,Business,Location,Neighborhood
# Register your models here.

admin.site.register(Profile)
admin.site.register(Posts)
admin.site.register(Business)
admin.site.register(Location)
admin.site.register(Neighborhood)
