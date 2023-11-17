
from django.urls import path, include
from .views import home,puntos,registro,login

urlpatterns = [
    path('', home, name = 'home'),
    path('puntos',puntos, name = 'puntos'),
    path('registro', registro , name = 'registro'),
    path('login', login , name = 'login'),
    
]