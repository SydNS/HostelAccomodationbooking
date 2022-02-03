from django.contrib import admin
from django.urls import path, include
from . import views

app_name="hostels"
urlpatterns = [

    path('hostels', views.hostels, name='hostels'),
    path('record_hostel/', views.makehostels, name='record_hostel'),
    path('edit_hostel/<int:id>/', views.edithostel, name='edit_hostel'),
    # # bookings details
    path('hostel/<int:id>/', views.hostel_details, name='hostel_details'),
    # # bookings deletion
    path('delete_hostel/<int:id>/', views.hostel_delete, name='delete_hostel'),
    # path('Bookings/<int:id>/', views.Bookings, name='Bookings_Details'),
    #
    # path('delete_bookings/<int:id>/', views.Bookings, name='Delete_Bookings'),


]
