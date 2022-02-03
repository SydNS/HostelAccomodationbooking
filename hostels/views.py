# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

from .forms import HostelForm
from .models import Hostel
from roomsapp.models import Roommodel
from useraccounts.models import Student


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
#     arrival_date = models.DateField(null=True, blank=True)
#     payment_status = models.CharField(max_length=10, choices=PAYMENT_CHOICES)

# Create your create-views here.
# @login_required
def hostels(request):
    hostelsobj = Hostel.objects.all()
    roomsobj = Roommodel.objects.all()
    studentlistobj = Student.objects.all()

    print(len(roomsobj))
    if request.method == "POST":
        bookingform = HostelForm(request.POST)
        if bookingform.is_valid():
            bookingform_ = bookingform.save(commit=True)

            return HttpResponseRedirect('hostels')
        else:
            return HttpResponseRedirect('hostels')


    else:
        if not hostelsobj:
            return render(request=request, template_name="dashboard/hostel/hostelslistandimages.html",
                          context={'hostelsobj': {}
                                   }
                          )
        else:
            # totalhostels overall
            totalhostels = hostelsobj.count()
            formpassed = HostelForm()

            # room types available     roomsobj = Roommodel.objects.all()
            numberofrooms = roomsobj.count
            singlerooms = roomsobj.filter(room_capacity="Single").count
            doublerooms = roomsobj.filter(room_capacity="Double").count

            Booked = roomsobj.filter(availbilitystatus="Booked").count
            Vacant = roomsobj.filter(availbilitystatus="Vacant").count
            Half_full = roomsobj.filter(availbilitystatus="Booked").count
            Filled = roomsobj.filter(availbilitystatus="Filled").count

            return render(request=request, template_name='dashboard/hostel/hostelslistandimages.html'
                          , context={
                    'hostelsobj': hostelsobj,
                    'totalhostels': totalhostels,
                    'addhostelform': formpassed,

                    # rooms information
                    'roomsobj': roomsobj,
                    'numberofrooms': numberofrooms,

                    # type
                    'singlerooms': singlerooms,
                    'doublerooms': doublerooms,

                    # availbilitystatus
                    'Booked': Booked,
                    'Vacant': Vacant,
                    'Half_full': Half_full,
                    'Filled': Filled,

                }
                          )


# Create your views here.
@login_required
def hostel(request):
    hostelsobj = Hostel.objects.all()
    if not hostelsobj:
        return render(request=request, template_name="dashboard/hostel/hostels.html",
                      context={'hostelsobj': {}
                               }
                      )
    else:
        numberofbooking = hostelsobj.count
        return render(request=request, template_name='dashboard/hostel/hostels.html',
                      context={
                          'hostelsobj': hostelsobj,
                          'numberofbooking': numberofbooking,
                      })


# Create your create-views here.
@login_required
def makehostels(request):
    formpassed = HostelForm()
    if request.method == "POST":
        bookingform = HostelForm(request.POST, request.FILES)

        # print(bookingform)
        if bookingform.is_valid():
            bookingform.save()
            print(bookingform)
            return redirect('hostels:hostels')

    return render(request=request, template_name='dashboard/hostel/add_new_hostel.html',
                      context={'form': formpassed})


# Create your edit-views here.bookingform_
@login_required
def edithostel(request, id):
    bookingeditable = get_object_or_404(HostelForm, id=id)
    return render(request=request, template_name='dashboard/hostel/booking-edit.html',
                  context={'bookingeditable': bookingeditable}
                  )


# Create your views here.
@login_required
def hostel_details(request, id):
    hostel_details = get_object_or_404(Hostel, id=id)
    ratings = hostel_details.ratings
    return render(request=request, template_name='dashboard/hostel/hosteldetails.html',
                  context={
                      'hostel_details': hostel_details,
                      'ratings': range(ratings),
                  }
                  )


# Create your views here.
@login_required
def hostel_delete(request, id):
    bookingdetails = get_object_or_404(Hostel, id=id)

    return render(request=request, template_name='dashboard/hostel/booking-edit.html',
                  context={'bookingeditable': bookingdetails}
                  )
