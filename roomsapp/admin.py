from django.contrib import admin
from .models import Roommodel


# Register your models here.

# room_no = models.IntegerField()
# gender = models.CharField(max_length=8, choices=GENDER)
# room_capacity = models.CharField(max_length=10, choices=ROOM_TYPE)
# meal = models.CharField(max_length=5, choices=MEALS_STATUS)
# rentfee = models.IntegerField(max_length=8)
# availbilitystatus = models.CharField(max_length=10, choices=BOOKING_STATUS)
# photo = models.CharField(max_length=225)
#

@admin.register(Roommodel)
class RoommodelAdmmin(admin.ModelAdmin):
    list_filter = ('gender', 'room_capacity', 'availbilitystatus',)
    list_display = ('room_no','gender', 'room_capacity', 'availbilitystatus',)
    search_fields = ('room_no', 'room_capacity',)
