
from django.urls import path
#-->Importamos las Vistas para las URL
from .views import *


urlpatterns = [
    path('',Home,name='inicio'),
    path('agregar', Agregar, name='Agregar'),
    path('logout', salir, name='logout'),
]
