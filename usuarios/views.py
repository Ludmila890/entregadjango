from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import CreacionDeUsuario, EditarPerfilForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtras
from .forms import EditarPerfilForm


def login(request):
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            
            user = authenticate(request, username=usuario, password=contrasenia)
            
            django_login(request, user)
            
            return redirect('inicio')  
    
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
    formulario = CreacionDeUsuario()
    
    if request.method == "POST":
        formulario = CreacionDeUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

def perfil(request):
    return render(request,'usuarios/perfil.html')

from .forms import EditarPerfilForm

def editar_perfil(request):
    usuario = request.user
    usuario_datos_extras, creado = DatosExtras.objects.get_or_create(user=usuario)

    if request.method == "POST":
        formulario = EditarPerfilForm(request.POST, request.FILES, instance=usuario_datos_extras)
        if formulario.is_valid():
            formulario.save()
            return redirect('perfil')
    else:
        formulario = EditarPerfilForm(instance=usuario_datos_extras)
    
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

class EditarContrasenia(PasswordChangeView):
    template_name = 'usuarios/cambiar_contrasenia.html'
    succes_urls = reverse_lazy('perfil')
    
#def perfil(request):
#    usuario = request.user  # Obtener el usuario actual
#    datos_extra = DatosExtras.objects.get(user=usuario)  # Obtener los datos extra del usuario
#    
#    return render(request, 'perfil.html', {'usuario': usuario, 'datos_extra': datos_extra})