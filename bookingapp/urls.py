from django.contrib import admin
from django.urls import path, include
from . import views

app_name="bookingapp"
urlpatterns = [

    path('', views.index, name='indexroute'),
    path('bookings/', views.bookings, name='Bookings'),
    path('make_booking/', views.makebookings, name='Make_Bookings'),
    path('edit_bookings/<int:id>/', views.editbookings, name='Edit_Bookings'),
    # # bookings details
    path('bookings/<int:id>/', views.bookings_details, name='bookings_details'),
    # # bookings deletion
    path('bookings/<int:id>/', views.bookings_delete, name='bookings_delete'),
    # path('Bookings/<int:id>/', views.Bookings, name='Bookings_Details'),
    #
    # path('delete_bookings/<int:id>/', views.Bookings, name='Delete_Bookings'),


]
