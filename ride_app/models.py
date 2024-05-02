from django.db import models
from accounts.models import User
from django.contrib.gis.db.models import PointField

STATUS_CHOICES = (
    ("REQUESTED","requested"),
    ("ACCEPTED","accepted"),
    ("STARTED", "started"),
    ("COMPLETED", "completed"),
    ("CANCELLED", "cancelled")
)

VEHICLE_CHOICES = (
    ("ALL","all"),
    ("CAR","car"),
    ("BIKE","bike"),
    ("AUTO", "auto")
)
class Ride(models.Model):

    rider = models.ForeignKey(User,on_delete=models.CASCADE,related_name='rides_as_rider')
    driver =models.ForeignKey(User,on_delete=models.CASCADE,related_name='rides_as_driver')
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES,default="REQUESTED")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    current_location = PointField(null=True, blank=True, spatial_index=True, geography=True)
    vehicle=models.CharField(max_length=30,choices=VEHICLE_CHOICES,default='ALL')

    def __str__(self):
        return f'Ride from {self.pickup_location} to {self.dropoff_location}'
    

