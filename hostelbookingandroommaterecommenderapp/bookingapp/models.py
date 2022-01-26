from django.db import models


# Create your models here.

class Bookhosteltable(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
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
    seater = models.IntegerField()
    food = models.CharField(max_length=20)
    room_alloted = models.IntegerField()
    price = models.IntegerField()
    booked_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'bookhostel_table'
