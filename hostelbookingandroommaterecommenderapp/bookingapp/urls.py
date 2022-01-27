from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    # path('', views.dashboard, name='dashboard'),
    # path('login/', views.loginuser, name='login'),
    # path('register/', views.Registering, name='register'),
    # path('logout/', views.Logout, name='logout'),
    #
    # Auditor of auditors
    path('bookings/', views.bookings, name='Bookings'),
    path('make_booking/', views.makebookings, name='Make_Bookings'),
    path('edit_bookings/<int:id>/', views.editbookings, name='Edit_Bookings'),
    # # bookings details
    # path('Bookings/<int:id>/', views.Bookings, name='Bookings_Details'),
    #
    # path('delete_bookings/<int:id>/', views.Bookings, name='Delete_Bookings'),


]
