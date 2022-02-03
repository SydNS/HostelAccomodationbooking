from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

from .forms import RoomForm
from hostels.models import Hostel
from .models import Roommodel
from useraccounts.models import Student


# Create your create-views here.
@login_required
def rooms(request):
    hostelsobj = Hostel.objects.all()
    roomsobj = Roommodel.objects.all()
    studentlistobj = Student.objects.all()

    print(len(roomsobj))
    if request.method == "POST":
        formpassed = RoomForm(request.POST)
        if formpassed.is_valid():
            bookingform_ = formpassed.save(commit=True)
            bookingform_.save()
            return HttpResponseRedirect('hostels')
    else:
        if not roomsobj:
            formpassed = RoomForm()
            return render(request=request, template_name="dashboard/hostel/rooms-list.html",
                          context={'roomsobj': {}, 'formpassed': formpassed}
                          )
        else:
            # totalhostels overall
            totalhostels = hostelsobj.count()
            formpassed = RoomForm()

            # room types available     roomsobj = Roommodel.objects.all()
            numberofrooms = roomsobj.count
            singlerooms = roomsobj.filter(room_capacity="Single").count
            doublerooms = roomsobj.filter(room_capacity="Double").count

            # meals
            roomsobjwithmeals = roomsobj.filter(meal="Yes")
            roomsobjwithnomeals = roomsobj.filter(meal="No")

            # availability
            Booked = roomsobj.filter(availbilitystatus="Booked").count
            Vacant = roomsobj.filter(availbilitystatus="Vacant").count
            Half_full = roomsobj.filter(availbilitystatus="Booked").count
            Filled = roomsobj.filter(availbilitystatus="Filled").count

            return render(request=request, template_name='dashboard/hostel/rooms-list.html'
                          , context={
                    'hostelsobj': hostelsobj,
                    'totalhostels': totalhostels,
                    'formpassed': formpassed,

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


@login_required
def add_room(request):
    formpassed = RoomForm()
    if request.method == "POST":
        roomform = RoomForm(request.POST)
        if roomform.is_valid():
            roomform_ = roomform.save(commit=True)
            roomform_.save()
            return redirect('rooms')
    else:
        return render(request=request, template_name='dashboard/hostel/booking-add.html', context={'form': formpassed})


# Create your edit-views here.bookingform_
@login_required
def edit_room(request, id):
    bookingeditable = get_object_or_404(RoomForm, id=id)
    return render(request=request, template_name='dashboard/hostel/booking-edit.html',
                  context={'bookingeditable': bookingeditable}
                  )


# Create your views here.
@login_required
def room_details(request, id):
    hostel_details = get_object_or_404(Roommodel, id=id)
    ratings = hostel_details.ratings
    return render(request=request, template_name='dashboard/hostel/hosteldetails.html',
                  context={
                      'hostel_details': hostel_details,
                      'ratings': range(ratings),
                  }
                  )


# Create your views here.
@login_required
def delete_room(request, id):
    room_to_delete = get_object_or_404(Roommodel, id=id)
    if request.method == "POST":
        room_to_delete.delete()
        return redirect('rooms')

    return render(request=request, template_name='dashboard/hostel/room-delete.html',
                  context={'room_to_delete': room_to_delete}
                  )
