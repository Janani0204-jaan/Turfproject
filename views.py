from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Turf
from django.http import HttpResponse
from django.db.models import Count, Avg
from .models import Booking


# Create your views here.


def home(request):
    return render(request, 'turf.html')

def booking(request):
    return render(request,'booking.html')

def allturfs(request):
    return render(request, 'allturfs.html')

def contacts(request):
    return render(request, 'contact.html')

def events(request):
    return render(request, 'events.html')
def payment(request):
    return render(request, 'payment.html')
def bookingconfirmation(request):
    return render(request, 'payment.html')
def confirmation(request):
    return render(request, 'payment.html')
def draft(request):
    return render(request, 'draft.html')




from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookingForm




def bookingview(request):
    turfs = Turf.objects.all()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        action = request.POST.get('action')

        if form.is_valid():
            booking = form.save(commit=False)
            booking.amount = booking.turf.rate
            if action == 'confirm':
                booking.is_booked = True
                booking.save()
                return redirect('bookingconfirmation')

            elif action == 'save':
                booking.save()
                return render(request, 'draft.html')

    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form, 'turfs': turfs})




from django.shortcuts import render, redirect
from .forms import QuickMessageForm

def quick_message_view(request):
    if request.method == 'POST':
        form = QuickMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Thank you.html')
    else:
        form = QuickMessageForm()
    return render(request, 'contact.html', {'form': form})


from django.shortcuts import render
from .models import Booking, Turf
from datetime import datetime
from django.db.models import Count, Avg



from datetime import datetime, time
from django.db.models import Count, Avg
from .models import Booking

def team_list_view(request):
    selected_date = request.GET.get('date')

    if selected_date:
        try:

            date_obj = datetime.strptime(selected_date, "%Y-%m-%d")
            start_datetime = datetime.combine(date_obj.date(), time.min)
            end_datetime = datetime.combine(date_obj.date(), time.max)
            bookings = Booking.objects.filter(booking_date__range=(start_datetime, end_datetime))
        except Exception as e:
            print("Date parsing error:", e)
            bookings = Booking.objects.none()
    else:
        bookings = Booking.objects.all()

    teams = bookings.values_list('team_name', 'turf__name', 'slot', 'amount')
    total_teams = bookings.values('team_name').distinct().count()
    total_slots = bookings.count()

    turf_counts = bookings.values('turf__name').annotate(count=Count('turf__name')).order_by('-count')
    most_popular_turf = turf_counts[0]['turf__name'] if turf_counts else 'N/A'

    average_slot_amount = bookings.aggregate(avg=Avg('amount'))['avg'] or 0

    context = {
        'teams': teams,
        'total_teams': total_teams,
        'total_slots': total_slots,
        'most_popular_turf': most_popular_turf,
        'average_slot_amount': round(average_slot_amount, 2),
        'selected_date': selected_date,
    }

    return render(request, 'print_teams.html', context)




