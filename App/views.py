from django.shortcuts import render
from .forms import * 
from .models import *

# Create your views here.
def Home(request):
    buscar=Vehiculo.objects.all().order_by('-Codigo')[:4]
    data={
        'forms':buscar
    }
    return render (request,'index.html',data)

def Agregar(request):
    data={
        'forms':Vehiculo()
    }
    if request.method=='POST':
        query=Vehiculo(data=request.POST, files=request.FILES)
        if query.is_valid():
                query.save()
                data['mensaje']="Datos Guardados"
        else:
                data['forms']=Vehiculo
            
    return render (request,'pages/Agregar.html', data)