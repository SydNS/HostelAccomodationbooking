from django.db import models
from django.contrib.auth.models import AbstractUser,User


# Create your models here.
# ID
# Customer
# Package
# Booking
# Room Type
# Arrive
# Payment

class Bookhosteltable(models.Model):
    uid = models.CharField(max_length=40)
    course = models.CharField(max_length=35)
    emergency_no = models.IntegerField()
    guardian_name = models.CharField(max_length=100)
    guardian_relation = models.CharField(max_length=100)
    guardian_no = models.CharField(max_length=20)
    guardian_address = models.CharField(max_length=255)
    duration = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    room_capacity = models.IntegerField()
    food = models.CharField(max_length=20)
    room_alloted = models.IntegerField()
    price = models.IntegerField()
    booked_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'bookhostel_table'
