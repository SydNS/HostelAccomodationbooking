from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Bookhosteltable


# class Bookhosteltable(models.Model):
#     uid = models.CharField(max_length=40)
#     course = models.CharField(max_length=35)
#     emergency_no = models.IntegerField()
#     guardian_name = models.CharField(max_length=100)
#     guardian_relation = models.CharField(max_length=100)
#     guardian_no = models.CharField(max_length=20)
#     guardian_address = models.CharField(max_length=255)
#     duration = models.IntegerField()
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=100)
#     pincode = models.CharField(max_length=20)
#     seater = models.IntegerField()
#     food = models.CharField(max_length=20)
#     room_alloted = models.IntegerField()
#     price = models.IntegerField()
#     booked_time = models.DateTimeField()
#


# Create your views here.
def bookings(request):
    bookingslist = get_list_or_404(Bookhosteltable)

    for object in bookingslist:
        totalprice =+ object.price
    return render(request=request, template_name='dashboard/hostel/index.html',
                  context={'bookingslist': bookingslist, 'totalprice': totalprice})


# Create your create-views here.
def makebookings(request):
    return render(request=request, template_name='dashboard/hostel/booking-add.html')


# Create your edit-views here.
def editbookings(request, id):
    bookingeditable = get_object_or_404(Bookhosteltable, id=id)
    return render(request=request, template_name='dashboard/hostel/booking-edit.html',
                  context={'bookingeditable': bookingeditable}
                  )
