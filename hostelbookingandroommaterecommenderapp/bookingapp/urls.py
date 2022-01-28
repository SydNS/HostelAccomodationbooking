from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='indexroute'),
    path('bookings/', views.bookings, name='Bookings'),
    path('make_booking/', views.makebookings, name='Make_Bookings'),
    path('edit_bookings/<int:id>/', views.editbookings, name='Edit_Bookings'),
    # # bookings details
    # path('Bookings/<int:id>/', views.Bookings, name='Bookings_Details'),
    #
    # path('delete_bookings/<int:id>/', views.Bookings, name='Delete_Bookings'),


]
