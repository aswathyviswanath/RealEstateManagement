from django.contrib import admin
from .models import Ride
# Register your models here.

class RideAdmin(admin.ModelAdmin):
    list_display = ('__str__',"rider", "driver", "current_location","pickup_location","dropoff_location","vehicle")

admin.site.register(Ride,RideAdmin)