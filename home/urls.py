from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("", views.homepage),
    path("about/", views.aboutPage),
    path("details/<int:id>", views.detailsPage),
    path("myBookings/", views.myBookings),
]