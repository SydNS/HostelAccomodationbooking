from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "roomsapp"
urlpatterns = [

    path('rooms', views.rooms, name='rooms'),
    path('add_room/', views.add_room, name='add_room'),
    path('edit_room/<int:id>/', views.edit_room, name='edit_room'),
    # # room details
    path('room/<int:id>/', views.room_details, name='room'),
    # # room deletion
    path('delete_room/<int:id>/', views.delete_room, name='delete_room'),

]
