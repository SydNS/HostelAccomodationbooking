from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "rooms"
urlpatterns = [

    path('rooms', views.rooms, name='hostels'),
    path('add_room/', views.add_room, name='Make_Bookings'),
    path('edit_room/<int:id>/', views.edit_room, name='Edit_Bookings'),
    # # room details
    path('room/<int:id>/', views.room_details, name='hostel_details'),
    # # room deletion
    path('delete_room/<int:id>/', views.delete_room, name='hostel_delete'),

]
