from random import choices

from django.db import models

from django.contrib.auth.models import AbstractUser, User


# Create your models here.
# ID
# Customer
# Package
# Booking
# Room Type
# Arrive
# Payment

class Bookhosteltable(models.Model):
    PAYMENT_CHOICES = [
        ('PAID', 'PAID'),
        ('DUE', 'DUE'),
    ]
    uid = models.CharField(max_length=40)
    customer_name = models.ForeignKey('useraccounts.Student', on_delete=models.CASCADE)
    room_type = models.ForeignKey('roomsapp.Roommodel', on_delete=models.CASCADE)
    duration = models.IntegerField()
    booked = models.BooleanField(default=False)
    arrival_date = models.DateField(null=True, blank=True)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_CHOICES)

    class Meta:
        managed = True
        db_table = 'bookhostel_table'
