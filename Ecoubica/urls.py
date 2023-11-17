
from django.urls import path
from .views import home,puntos

urlpatterns = [
    path('', home, name = 'home'),
    path('puntos',puntos, name = 'puntos'),
    
]