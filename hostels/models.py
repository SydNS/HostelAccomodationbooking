from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class Hostel(models.Model):
    RATING_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=50)
    total_rooms = models.IntegerField(default=0)  # total rooms in the hostel
    total_available_rooms = models.IntegerField(default=0)  # total available rooms for booking purposes
    total_booked_rooms = models.IntegerField(default=0)  # total rooms that are already booked
    ratings = models.IntegerField(default=1, choices=RATING_CHOICES)  # total rooms that are already booked
    number_of_singlerooms = models.IntegerField()  # total rooms that are already booked
    number_of_doublerooms = models.IntegerField()
    singleroom_price = models.IntegerField(default=1500000)  # total rooms that are already booked
    doubleroom_price = models.IntegerField(default=2000000)  # total rooms that are already booked

    def __str__(self):
        return self.name

    def available_rooms(self):
        return self.total_available_rooms
