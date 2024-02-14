from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Empleados
from inicio.forms import formularioCreacionEmpleados

def inicio(request):
    return render(request, 'inicio.html')

def lista_empleados(request,):
        empleado = Empleados.objects.all()
        
        return render(request,'lista_empleados.html', {'empleado':empleado})

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
        
    return render(request,'crear_empleado.html', {'formulario': formulario})