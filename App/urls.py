
from django.urls import path
#-->Importamos las Vistas para las URL
from .views import *


urlpatterns = [
    path('',Home,name='inicio'),
]
