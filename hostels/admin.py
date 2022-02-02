from django.contrib import admin

# Register your models here.
from .models import Hostel


class HostelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'total_rooms','location', 'total_available_rooms', 'total_booked_rooms', 'singleroom_price', 'doubleroom_price','photo', 'ratings', 'number_of_singlerooms', 'number_of_doublerooms')


admin.site.register(Hostel, HostelAdmin)