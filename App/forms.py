#-->importamos Forms
from django import forms
#-->importamos los modelos/tablas
from .models import *

class NuevoVehiculo(forms.ModelForm):
    class Meta:
        model=Vehiculo
        fields='__all__'