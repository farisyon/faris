from django.contrib import admin 
from  .models import Slot, User,Booking
# Register your models here.

admin.site.register(User)
admin.site.register(Slot)
admin.site.register(Booking)
