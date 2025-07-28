from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from venue.models import Space
from bookings.forms import BookingForm
from django.contrib import messages
from .models import Booking

def book_space(request, space_id):
    space = get_object_or_404(Space, id=space_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.space = space
            booking.user = request.user  # If using login
            space.is_booked = True
            space.save()
            booking.save()
            return redirect('bookings:booking_list')  # Or your desired page
                 
    else:
        form = BookingForm()
    return render(request, 'bookings/book_space.html', {'form': form, 'space': space})

def booking_list(request):
    if request.user.is_superuser:
        bookings = Booking.objects.select_related('venue', 'user').all()

    else:
        bookings = Booking.objects.select_related('venue').filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

