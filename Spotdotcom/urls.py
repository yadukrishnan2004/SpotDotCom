"""
URL configuration for ProjectSpot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from Spotdotcom.views import*
urlpatterns = [
    path('',Login.as_view(),name="login"),
    # ////////////////////////// ADMIN /////////////////////////////////////////////////

    path('adminhome',admindashboard.as_view(),name="admindashboard"),
    path('userlist',userlist.as_view(),name="userlist"),
    path('manage_tourist',manage_tourist.as_view(),name="manage_tourist"),
    path('manage_Restaurent', manage_Restaurent.as_view(),name="manage_Restaurent"),
    path('manage_Resort', manage_Resort.as_view(),name="manage_Resort"),
    path('manage_photoarea', manage_photoarea.as_view(),name="manage_photoarea"),
    path('manage_ParkingSpot', manage_ParkingSpot.as_view(),name="manage_ParkingSpot"),
    path('manage_Amalgamation', manage_Amalgamation.as_view(),name="manage_Amalgamation"),
    path('deleteamal/<int:id>/', deleteamal.as_view(), name='deleteamal'),
    path('deletepark/<int:id>/', deletepark.as_view(), name='deletepark'),
    path('deletephoto/<int:id>/', deletephoto.as_view(), name='deletephoto'),
    path('deleteresort/<int:id>/', deleteresort.as_view(), name='deleteresort'),
    path('deletetourist/<int:id>/', deletetourist.as_view(), name='deletetourist'),
    path('deleteuser/<int:id>/', deleteuser.as_view(), name='deleteuser'),

    # /////////////////////////////////// RESTAURANT ////////////////////////////////////////////////

    path('RestaurantDash',RestaurantDash.as_view(),name="RestaurantDash"),
    path('RestaurantGallery',RestaurantGallery.as_view(),name="RestaurantGallery"),

]
