# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from random import choices

from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'admin'


class Blog(models.Model):
    title = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'blog'


class Bookhostel(models.Model):
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
    room_capacity = models.IntegerField()
    food = models.CharField(max_length=20)
    room_alloted = models.IntegerField()
    price = models.IntegerField()
    booked_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'bookhostel'


class Feedback(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    subject = models.CharField(max_length=255)
    feedback = models.TextField()
    created_at = models.DateTimeField()
    replied = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'feedback'


class Notes(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    title = models.CharField(max_length=255)
    note = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'notes'


class Notification(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    type = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'notification'


class Registration(models.Model):
    roomno = models.IntegerField(blank=True, null=True)
    room_capacity = models.IntegerField(blank=True, null=True)
    feespm = models.IntegerField(blank=True, null=True)
    foodstatus = models.CharField(max_length=30)
    stayfrom = models.DateField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    course = models.CharField(max_length=500, blank=True, null=True)
    regno = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(db_column='firstName', max_length=500, blank=True,
                                 null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='middleName', max_length=500, blank=True,
                                  null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=500, blank=True,
                                null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=250, blank=True, null=True)
    contactno = models.BigIntegerField(blank=True, null=True)
    emailid = models.CharField(max_length=500, blank=True, null=True)
    egycontactno = models.BigIntegerField(blank=True, null=True)
    guardianname = models.CharField(db_column='guardianName', max_length=500, blank=True,
                                    null=True)  # Field name made lowercase.
    guardianrelation = models.CharField(db_column='guardianRelation', max_length=500, blank=True,
                                        null=True)  # Field name made lowercase.
    guardiancontactno = models.BigIntegerField(db_column='guardianContactno', blank=True,
                                               null=True)  # Field name made lowercase.
    corresaddress = models.CharField(db_column='corresAddress', max_length=500, blank=True,
                                     null=True)  # Field name made lowercase.
    correscity = models.CharField(db_column='corresCIty', max_length=500, blank=True,
                                  null=True)  # Field name made lowercase.
    corresstate = models.CharField(db_column='corresState', max_length=500, blank=True,
                                   null=True)  # Field name made lowercase.
    correspincode = models.IntegerField(db_column='corresPincode', blank=True, null=True)  # Field name made lowercase.
    pmntaddress = models.CharField(db_column='pmntAddress', max_length=500, blank=True,
                                   null=True)  # Field name made lowercase.
    pmntcity = models.CharField(db_column='pmntCity', max_length=500, blank=True,
                                null=True)  # Field name made lowercase.
    pmnatetstate = models.CharField(db_column='pmnatetState', max_length=500, blank=True,
                                    null=True)  # Field name made lowercase.
    pmntpincode = models.IntegerField(db_column='pmntPincode', blank=True, null=True)  # Field name made lowercase.
    postingdate = models.DateTimeField(db_column='postingDate', blank=True, null=True)  # Field name made lowercase.
    updationdate = models.CharField(db_column='updationDate', max_length=500, blank=True,
                                    null=True)  # Field name made lowercase.
    photo = models.CharField(max_length=225)

    class Meta:
        managed = True
        db_table = 'registration'


class RoomLogs(models.Model):
    hid = models.ForeignKey(Bookhostel, models.DO_NOTHING, db_column='hid')
    roomno = models.IntegerField()
    allot_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'room_logs'


# =======================rooms======================================
# Room No.
# Room Type
# AC/Non AC
# Meal
# Bed Capacity
# Rent
# Status
# class Person(models.Model):
#     SHIRT_SIZES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#     )
#     name = models.CharField(max_length=60)
#     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Rooms(models.Model):
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

    room_no = models.IntegerField()
    gender = models.CharField(max_length=8, choices=GENDER)
    room_capacity = models.CharField(max_length=10, choices=ROOM_TYPE)
    meal = models.CharField(max_length=5, choices=MEALS_STATUS)
    rentfee = models.IntegerField(max_length=8)
    availbilitystatus = models.CharField(max_length=10, choices=BOOKING_STATUS)
    photo = models.CharField(max_length=225)


    class Meta:
        managed = True
        db_table = 'rooms'


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    photo = models.CharField(max_length=225)
    token = models.CharField(max_length=100)
    token_expire = models.DateTimeField()
    created_at = models.DateTimeField()
    verified = models.IntegerField()
    deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'


class Visitors(models.Model):
    id = models.IntegerField()
    hits = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'visitors'
