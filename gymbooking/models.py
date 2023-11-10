from django.db import models

class User (models.Model):
    userid = models.CharField(max_length=12,primary_key=True) 
    username = models.TextField(max_length=100)
    usergender= models.TextField(max_length=100)
    usercategory= models.TextField(max_length=100)
    userphone = models.IntegerField(null=False) 

class Slot (models.Model):
    slotid = models.CharField(max_length=12,primary_key=True) 
    shift = models.TextField(max_length=100)
    time =models.TextField(max_length=100)

class Booking(models.Model):
    id=models.IntegerField(blank=True,primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    slotid = models.ForeignKey(Slot, on_delete=models.CASCADE)
    date = models.TextField(max_length=100)
    notes = models.TextField(max_length=255, blank=True)