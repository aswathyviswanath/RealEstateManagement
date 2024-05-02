from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Driver', 'Driver'),
        ('Passenger', 'Passenger'),
    )
    user_type = models.CharField(max_length=30, choices=USER_TYPE_CHOICES, blank=True, null=True,default='Passenger')

 