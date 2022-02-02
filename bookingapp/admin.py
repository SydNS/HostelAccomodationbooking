from django.contrib import admin

# Register your models here.

from .models import Bookhosteltable


@admin.register(Bookhosteltable)
class BookhosteltableAdmin(admin.ModelAdmin):
    list_display = ('uid',   'customer_name', 'room_type', 'duration', 'payment_status','arrival_date', )
    list_filter = ('uid',  'customer_name', 'room_type', 'duration','payment_status','arrival_date',)
    search_fields = ('uid',   'customer_name', 'room_type', 'duration', 'payment_status','arrival_date',)

#
# class Bookhosteltable(models.Model):
#     PAYMENT_CHOICES = [
#         ('PAID', 'PAID'),
#         ('DUE', 'DUE'),
#     ]
#     uid = models.CharField(max_length=40)
#     customer_name = models.ForeignKey('useraccounts.Student', on_delete=models.CASCADE)
#     room_type = models.ForeignKey('roomsapp.Roommodel', on_delete=models.CASCADE)
#     duration = models.IntegerField()
#     booked = models.BooleanField(default=False)
#    'booked','arrival_date' = models.DateField(null=True, blank=True)
#     payment_status = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
#
