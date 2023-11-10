from django.shortcuts import render, redirect
from .models import User
from .models import Slot
from .models import Booking
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render (request,"index.html")
def booking(request):
    return render (request,"booking.html")
def schedule(request):
    return render (request,"schedule.html")
def slot(request):
    # Get all the slot objects from the database
    slots = Slot.objects.all()
    
    context = {
        'slots': slots
    }
    return render(request, 'slot.html', context)

def userdetail(request):
    if request.method == 'POST':
        XuserID = request.POST['userid']
        Xusername = request.POST['username']
        Xusergender = request.POST['usergender']
        Xusercat = request.POST['usercategory']
        XuserNo = request.POST['userphone']
        data = User(userid = XuserID, username = Xusername,usergender = Xusergender, usercategory = Xusercat, userphone = XuserNo)
        data.save()
        dict = {

        }
        return render(request, 'userdetail.html',dict)

    else:
        dict = {

        }
    return render (request,"userdetail.html")


def userbooking(request):
    if request.method == 'POST': 
        XXUSER = request.POST['userid']

        try:
            XuserID = User.objects.get(userid=XXUSER)
        except User.DoesNotExist:
            # Handle the case where the user does not exist
            return render(request, 'userbooking.html', {'message': 'User does not exist.'})

        XXSLOT = request.POST.get('slotid', '')

        try:
            Xslot = Slot.objects.get(slotid=XXSLOT)
        except Slot.DoesNotExist:
            # Handle the case where the slot does not exist
            return render(request, 'userbooking.html', {'message': 'Slot does not exist.'})

        Xdate = request.POST['date']
        Xnotes = request.POST['notes']

        data = Booking(userid=XuserID, slotid=Xslot, date=Xdate, notes=Xnotes)
        data.save()

        return render(request, 'userbooking.html')

    else:
        dict = {
            # ...
        }
        return render(request, 'userbooking.html', dict)
    
# View to display the bookingdetail.html page
def bookingdetail(request):
    if request.method == 'POST':
        user_id = request.POST['userid']
        try:
            user = User.objects.get(userid=user_id)
            user_booking = Booking.objects.filter(userid=user)
            return render(request, 'bookingdetail.html', {'user_id': user_id, 'user_booking': user_booking})
        except User.DoesNotExist:
            error_message = "User not found."
            return render(request, 'bookingdetail.html', {'error_message': error_message})

    return render(request, 'bookingdetail.html')

# View to update the date for a booking
def update_date(request):
    if request.method == 'POST':
        booking_id = request.POST['booking_id']
        new_date = request.POST['new_date']
        booking = Booking.objects.get(id=booking_id)
        booking.date = new_date
        booking.save()

        return redirect('bookingdetail')

    return redirect('bookingdetail.html')

# View to delete the note for a booking
def delete_note(request):
    if request.method == 'POST':
        booking_id = request.POST['booking_id']

        booking = Booking.objects.get(id=booking_id)
        booking.notes = ""  # Clear the notes
        booking.save()

        return redirect('bookingdetail')

    return render(request, 'bookingdetail.html')