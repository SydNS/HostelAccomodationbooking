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
    LAVATORY_ = (
        ('In Room', 'In Room'),
        ('Outdoors', 'Outdoors'),
    )
    ROOM_CLASS = (
        ('Normal', 'Normal'),
        ('Executive', 'Executive'),
        ('Deluxe', 'Deluxe'),
    )

    room_no = models.CharField(max_length=4)
    hostel_name = models.ForeignKey("hostels.Hostel", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='hostels_rooms/')
    gender = models.CharField(max_length=8, choices=GENDER)
    lavatory = models.CharField(max_length=12, choices=LAVATORY_)
    room_capacity = models.CharField(max_length=10, choices=ROOM_TYPE)
    meal = models.CharField(max_length=5, choices=MEALS_STATUS)
    availbilitystatus = models.CharField(max_length=10, choices=BOOKING_STATUS)

    def __str__(self):
        return str(self.room_capacity)

    class Meta:
        managed = True
        db_table = 'rooms'
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

