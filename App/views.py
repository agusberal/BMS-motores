from django.shortcuts import render,get_object_or_404,redirect
from .forms import * 
from .models import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def Home(request):
    buscar=Vehiculo.objects.all().order_by('-Codigo')[:4]
    data={
        'forms':buscar
    }
    return render (request,'index.html',data)

@login_required
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



def salir(request):
    logout(request)
    return redirect(to='inicio')