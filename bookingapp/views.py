from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

from .forms import Bookhosteltableform
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
@login_required
def index(request):
    bookingslist = Bookhosteltable.objects.all()
    if not bookingslist:
        return render(request=request, template_name="dashboard/hostel/index.html",
                      context={'bookingslist': {},
                               'totalprice': 0,
                               'immediate_price_diff': 0,
                               'immediate_price_diff_sec_third': 0,
                               'firstprice': 0,
                               'lastprice': 0,

                               }
                      )
    else:
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

        return render(request=request, template_name='dashboard/hostel/index.html'
                      ,context={'bookingslist': bookingslist,
                               'totalprice': totalprice['price__sum'],
                               'immediate_price_diff': percentagepricechange,
                               'immediate_price_diff_sec_third': percentagepricechangethirdlast,
                               'firstprice': firstprice,
                               'lastprice': lastprice,

                               }
                      )


# Create your views here.
@login_required
def bookings(request):
    bookingslist = Bookhosteltable.objects.all()
    if not bookingslist:
        return render(request=request, template_name="dashboard/hostel/bookings.html",
                      context={'bookingslist': {},
                               'totalprice': 0,
                               'immediate_price_diff': 0,
                               'immediate_price_diff_sec_third': 0,
                               'firstprice': 0,
                               'lastprice': 0,

                               }
                      )
    else:

        return render(request=request, template_name='dashboard/hostel/bookings.html',
                  context={'bookingslist': bookingslist})


# Create your create-views here.
@login_required
def makebookings(request):
    if request.method == 'POST':
        bookingform = Bookhosteltableform(request.POST)
        if bookingform.is_valid():
            bookingform_ = bookingform.save(commit=True)
            return redirect('indexroute')
    else:
        formpassed = Bookhosteltableform()

    return render(request=request, template_name='dashboard/hostel/booking-add.html', context={'form': formpassed})

# def makebookings(request):
#     if request.method == "POST":
#         form = Bookhosteltableform(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('indexroute')
#     # else:
#
#     formpassed = Bookhosteltableform()
#     return render(request=request, template_name='dashboard/hostel/booking-add.html', context={'form': formpassed})



# Create your edit-views here.
@login_required
def editbookings(request, id):
    bookingeditable = get_object_or_404(Bookhosteltable, id=id)
    return render(request=request, template_name='dashboard/hostel/booking-edit.html',
                  context={'bookingeditable': bookingeditable}
                  )
