from django.urls import path
from . import views

urlpatterns = [
path("",views.index , name="index"),
path("booking",views.booking , name="booking"),
path("schedule",views.schedule , name="schedule"),
path("slot",views.slot , name="slot"),
path("userdetail",views.userdetail , name="userdetail"),
path("userbooking",views.userbooking, name="userbooking"),
path("bookingdetail",views.bookingdetail, name="bookingdetail"),
path('update_date/', views.update_date, name='update_date'),
path('delete_note/', views.delete_note, name='delete_note'),
]