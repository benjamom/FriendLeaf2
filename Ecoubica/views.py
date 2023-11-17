from django.shortcuts import render
import folium
from .models import location as LocationModel
from django.views import View

def home(request):

    locations = LocationModel.objects.all()

    initialMap = folium.Map(location=[-33.5000852,-70.6162928], zoom_start=14)

    for loc in locations:
        coordinates =(loc.lat, loc.lng)
        folium.Marker(coordinates, popup = 'Sucursal: '+ loc.name).add_to(initialMap)

    context ={'map': initialMap._repr_html_(), 'locations':locations}
    return render(request, 'map/home.html', context)

def puntos(request):
    
    loca = LocationModel.objects.all()
    
    
    return render(request,'map/puntos.html')

