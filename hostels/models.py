from django.db import models


# Create your models here.

class Hostel(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=50)
    total_rooms = models.IntegerField(default=0)  # total rooms in the hostel
    total_available_rooms = models.IntegerField(default=0)  # total available rooms for booking purposes
    total_booked_rooms = models.IntegerField(default=0)  # total rooms that are already booked

    def __str__(self):
        return self.name

    def available_rooms(self):
        return self.total_available_rooms
