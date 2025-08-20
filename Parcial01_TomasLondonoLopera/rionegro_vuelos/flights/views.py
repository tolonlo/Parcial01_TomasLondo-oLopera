
from django.shortcuts import render, redirect
from django.db.models import Avg
from .forms import FlightForm
from .models import Flight

def index(request):
    return render(request, 'flights/index.html')

def create_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm()
    return render(request, 'flights/flight_form.html', {'form': form})



def flight_list(request):
    flights = Flight.objects.order_by('price') #menor precio primero
    return render(request, 'flights/flight_list.html', {'flights': flights})



def flight_stats(request):
    nacionalesTotal = Flight.objects.filter(type=Flight.TYPE_NACIONAL).count()
    internacionalesTotal = Flight.objects.filter(type=Flight.TYPE_INTERNACIONAL).count()

    Prom_nacional = Flight.objects.filter(type=Flight.TYPE_NACIONAL).aggregate(Avg('price'))['price__avg'] #Stat de vuelo nacional
    Prom_internacional = Flight.objects.filter(type=Flight.TYPE_INTERNACIONAL).aggregate(Avg('price'))['price__avg']#Stat de vuelo internacional

    context = {
        'total_nacionales': nacionalesTotal,
        'total_internacionales': internacionalesTotal,
        'avg_nacional': Prom_nacional,
        'avg_internacional': Prom_internacional,
    }
    return render(request, 'flights/flight_stats.html', context)
