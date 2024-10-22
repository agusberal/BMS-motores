from django.shortcuts import render
from .forms import * 
from .models import *

# Create your views here.
def Home(request):
    buscar=Vehiculo.objects.all().order_by('-Codigo')[:3]
    data={
        'forms':buscar
    }
    return render (request,'index.html',data)