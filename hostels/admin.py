from django.contrib import admin

# Register your models here.
from .models import Hostel


class HostelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'total_rooms', 'total_available_rooms', 'total_booked_rooms')


admin.site.register(Hostel, HostelAdmin)