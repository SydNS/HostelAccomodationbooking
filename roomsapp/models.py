from django.db import models


# Create your models here.

class Roommodel(models.Model):
    MEALS_STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    BOOKING_STATUS = (
        ('Booked', 'Booked'),
        ('Vacant', 'Vacant'),
        ('Filled', 'Filled'),
        ('Half_full', 'Half_full'),
    )
    CAPACITY_STATUS = (
        ('Empty', 'Empty'),
        ('Filled', 'Filled'),
        ('Half_full', 'Half_full'),
    )
    ROOM_TYPE = (
        ('Double', 'Double'),
        ('Single', 'Single'),
        ('Triple', 'Triple'),
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    ROOM_CLASS = (
        ('Normal', 'Normal'),
        ('Executive', 'Executive'),
        ('Deluxe', 'Deluxe'),
    )

    room_no = models.IntegerField()
    gender = models.CharField(max_length=8, choices=GENDER)
    room_capacity = models.CharField(max_length=10, choices=ROOM_TYPE)
    meal = models.CharField(max_length=5, choices=MEALS_STATUS)
    rentfee = models.IntegerField(max_length=10)
    availbilitystatus = models.CharField(max_length=10, choices=BOOKING_STATUS)

    def __str__(self):
        return str(self.room_capacity)

    class Meta:
        managed = True
        db_table = 'rooms'
