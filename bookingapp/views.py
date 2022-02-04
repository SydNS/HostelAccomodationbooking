from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

from .forms import Bookhosteltableform
from .models import Bookhosteltable
from roomsapp.models import Roommodel
from useraccounts.models import Student
from hostels.models import Hostel



@login_required
def index(request):
    bookingslist = Bookhosteltable.objects.all()
    roomsobj = Roommodel.objects.all()
    studentlistobj = Student.objects.all()
    hostelsobj = Hostel.objects.all()
    numberofbooking = hostelsobj.count

    # print(len(roomsobj))

    if not bookingslist:
        return render(request=request, template_name="dashboard/hostel/index.html",
                      context={'bookingslist': {},
                               'totalprice': roomsobj,
                               'immediate_price_diff': 0,
                               'immediate_price_diff_sec_third': 0,
                               'firstprice': 0,
                               'lastprice': 0,
                               # hostels info
                               'hostelsobj': hostelsobj,
                               'numberofbooking': numberofbooking,

                               }
                      )
    else:
        # totalbookings overall
        totalbookings = bookingslist.count()

        # booking payment condition
        paid_totalbookings = bookingslist.filter(payment_status="PAID").count
        due_totalbookings = bookingslist.filter(payment_status="DUE").count

        # room types available     roomsobj = Roommodel.objects.all()
        numberofrooms = roomsobj.count
        singlerooms = roomsobj.filter(room_capacity="Single").count
        doublerooms = roomsobj.filter(room_capacity="Double").count

        Booked = roomsobj.filter(availbilitystatus="Booked").count
        Vacant = roomsobj.filter(availbilitystatus="Vacant").count
        Half_full = roomsobj.filter(availbilitystatus="Booked").count
        Filled = roomsobj.filter(availbilitystatus="Filled").count

        # students information

        students = studentlistobj.count

        # gender
        students_male = studentlistobj.filter(gender="male").count
        students_female = studentlistobj.filter(gender="female").count

        # level_of_study
        students_firstyear = studentlistobj.filter(level_of_study="FIRST_YEAR").count
        students_secondyear = studentlistobj.filter(level_of_study="SECOND_YEAR").count
        students_thridyear = studentlistobj.filter(level_of_study="THIRD_YEAR").count
        students_forthyear = studentlistobj.filter(level_of_study="FORTH_YEAR").count

        return render(request=request, template_name='dashboard/hostel/index.html'
                      , context={
                'bookingslist': bookingslist,
                'totalbookings': totalbookings,
                'paid_totalbookings': paid_totalbookings,
                'due_totalbookings': due_totalbookings,

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

                # students information
                'students': students,
                'students_male': students_male,
                'students_female': students_female,

                # student level_of_study
                'students_firstyear': students_firstyear,
                'students_secondyear': students_secondyear,
                'students_thridyear': students_thridyear,
                'students_forthyear': students_forthyear,

                # hostels info
                'hostelsobj': hostelsobj,
                'numberofbooking': numberofbooking,

            }
                      )


# Create your views here.
@login_required
def bookings(request):
    bookingslist = Bookhosteltable.objects.all()
    if not bookingslist:
        return render(request=request, template_name="dashboard/hostel/bookings.html",
                      context={'bookingslist': {}
                               }
                      )
    else:
        numberofbooking = bookingslist.count
        return render(request=request, template_name='dashboard/hostel/bookings.html',
                      context={
                          'bookingslist': bookingslist,
                          'numberofbooking': numberofbooking,
                      })


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


# Create your edit-views here.
@login_required
def editbookings(request, id):
    bookingeditable = get_object_or_404(Bookhosteltable, id=id)
    return render(request=request, template_name='dashboard/hostel/booking-edit.html',
                  context={'bookingeditable': bookingeditable}
                  )


# Create your views here.
@login_required
def bookings_details(request, id):
    bookingdetails = get_object_or_404(Bookhosteltable, id=id)
    return render(request=request, template_name='dashboard/hostel/booking-edit.html',
                  context={'bookingeditable': bookingdetails}
                  )


# Create your views here.
@login_required
def bookings_delete(request, id):
    bookingdetails = get_object_or_404(Bookhosteltable, id=id)

    return render(request=request, template_name='dashboard/hostel/booking-edit.html',
                  context={'bookingeditable': bookingdetails}
                  )


##########from details page#
# Create your create-views here.
@login_required
def makebookingsfromdetails(request, id):
    hostel_obj = Hostel.objects.get(id=id)
    if request.method == 'POST':
        bookingform = Bookhosteltableform(request.POST)
        if bookingform.is_valid():
            bookingform_ = bookingform.save(commit=True)
            return redirect('bookingapp:indexroute')
    else:
        hostel_obj = Hostel.objects.get(id=id)
        # print(hostel_obj)
        hostelName = hostel_obj
        userNamenow = request.user

        formpassed = Bookhosteltableform(initial={'hostel_name': hostelName, 'customer_name': userNamenow})

    return render(request=request, template_name='dashboard/hostel/booking-add.html', context={'form': formpassed})
