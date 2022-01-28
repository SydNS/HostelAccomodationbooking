from django.contrib.auth.models import User
from django.db.models import Sum
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

# Create your create-views here.
def index(request):
    bookingslist = get_list_or_404(Bookhosteltable)

    num = Bookhosteltable.objects.all()
    totalprice = Bookhosteltable.objects.all().aggregate(Sum('price'))

    # working on booking price difference
    firstprice = bookingslist[0].price
    lastprice = bookingslist[-1].price
    secondlastprice = bookingslist[-2].price
    thirdlastprice = bookingslist[-3].price
    immediate_price_diff = secondlastprice - lastprice

    #  percentage price difference
    percentagepricechange = round((immediate_price_diff / totalprice['price__sum']) * 100, 1)

    percentagepricechangethirdlast = round(((thirdlastprice - secondlastprice) / totalprice['price__sum']) * 100, 1)

    return render(request=request, template_name='dashboard/hostel/index.html',
                  context={'bookingslist': bookingslist,
                           'totalprice': totalprice['price__sum'],
                           'immediate_price_diff': percentagepricechange,
                           'immediate_price_diff_sec_third': percentagepricechangethirdlast,
                           'firstprice': firstprice,
                           'lastprice': lastprice,

                           })


# Create your views here.
def bookings(request):
    bookingslist = get_list_or_404(Bookhosteltable)

    return render(request=request, template_name='dashboard/hostel/bookings.html',
                  context={'bookingslist': bookingslist})


# Create your create-views here.
def makebookings(request):
    return render(request=request, template_name='dashboard/hostel/booking-add.html')


# Create your edit-views here.
def editbookings(request, id):
    bookingeditable = get_object_or_404(Bookhosteltable, id=id)
    return render(request=request, template_name='dashboard/hostel/booking-edit.html',
                  context={'bookingeditable': bookingeditable}
                  )
