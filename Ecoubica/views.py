from django.shortcuts import redirect, render
import folium

from Ecoubica.forms import PuntoForm
from .models import location as LocationModel


def home(request):

    locations = LocationModel.objects.all()
    initialMap = folium.Map(location=[-33.5000852,-70.6162928], zoom_start=14)

    for loc in locations:
        coordinates =(loc.lat, loc.lng)
        folium.Marker(coordinates, popup = 'Sucursal: '+ loc.name).add_to(initialMap)

    context ={'map': initialMap._repr_html_(), 'locations':locations}
    return render(request, 'map/home.html', context)


def puntos(request):
    locations = LocationModel.objects.all()
    context ={'locations':locations}
    return render(request,'map/puntos.html', context)



def registro(request):
    return render(request, 'registration/registro.html')

def login(request):
    return render(request, 'registration/login.html')

def agregar_punto(request):
    if request.method == 'POST':
        form = PuntoForm(request.POST)
        if form.is_valid():
            form.save()
            # Puedes agregar aquí la lógica para actualizar el mapa con el nuevo punto
            return redirect('home')
    else:
        form = PuntoForm()

    return render(request, 'map/agregar_punto.html', {'form': form})