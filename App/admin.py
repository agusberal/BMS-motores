from django.contrib import admin


#--->Traemos la Tablas desde MODELS
from .models import *

#---->traemos los formularios generales
from .forms import *



# Register your models here.
admin.site.register(NuevoVehiculo)

