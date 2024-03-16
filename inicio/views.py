from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Empleados
from inicio.forms import formularioCreacionEmpleados, BusquedaEmpleado, formularioEdicionEmpleados
import random
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'inicio/inicio.html')


def about(request):
    return render(request, 'inicio/about.html')


def lista_empleados(request):
    empleado = Empleados.objects.all()
    formulario = BusquedaEmpleado(request.GET)

    if request.method == "GET" and formulario.is_valid():
        empleado_a_buscar = formulario.cleaned_data.get('empleado')
        empleado = Empleados.objects.filter(empleado__icontains=empleado_a_buscar)

    return render(request, 'inicio/lista_empleados.html', {'lista_empleados': empleado, 'formulario': formulario})

    
    

def crear_empleado(request):
    formulario = formularioCreacionEmpleados()
    if request.method == "POST":
        formulario = formularioCreacionEmpleados(request.POST)
        if formulario.is_valid():
            empleado = formulario.cleaned_data.get('empleado')
            sector = formulario.cleaned_data.get('sector')
            jornada = formulario.cleaned_data.get('jornada')
            empleado = Empleados(empleado=empleado, sector=sector, jornada=jornada)
            empleado.save()
            return redirect("lista_empleados")
    return render(request, 'inicio/crear_empleado.html', {'formulario': formulario})

@login_required
def eliminar_empleados(request, id_empleado):
    empleado = Empleados.objects.get(id=id_empleado)
    empleado.delete()
    return redirect('lista_empleados')

@login_required
def editar_empleados(request, id_empleado):
    empleado = Empleados.objects.get(id=id_empleado)
    formulario = formularioEdicionEmpleados(initial={'empleado': empleado.empleado, 'sector': empleado.sector, 'jornada': empleado.jornada})
    
    if request.method == "POST":
        formulario = formularioEdicionEmpleados(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            empleado.empleado =info_nueva.get('empleado')
            empleado.sector =info_nueva.get('sector')
            empleado.jornada =info_nueva.get('jornada')
            
            empleado.save()
            
            return redirect("lista_empleados")
        
    return render(request, 'inicio/editar_empleados.html', {'empleado': empleado, 'formulario': formulario})


def ver_empleados(request, id_empleado):
    empleado = Empleados.objects.get(id=id_empleado)
    return render(request, 'inicio/ver_empleados.html', {'empleado': empleado})



