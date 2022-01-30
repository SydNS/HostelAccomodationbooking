from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('login/', views.loginuser, name='login'),
    path('register/', views.Registering, name='register'),
    path('logout/', views.Logout, name='logout'),

    path('profilesetup/', views.ProfileSetting, name='profilesetup'),

    path('profiledetails/', views.Profiledetails, name='profiledetails'),

    # path("", include("hostelbookingandroommaterecommenderapp.urls"),name="dashboard"),

]