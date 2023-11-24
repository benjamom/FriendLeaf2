
from django.urls import path, include
from .views import home,puntos,registro,login,agregar_punto

urlpatterns = [
    path('', home, name = 'home'),
    path('puntos',puntos, name = 'puntos'),
    path('registro', registro , name = 'registro'),
    path('login', login , name = 'login'),
    path('agregar_punto/', agregar_punto, name='agregar_punto'),
    
]