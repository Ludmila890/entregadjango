from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from fichaje.models import Horarios
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import HorariosForm

class HorariosList(ListView):
    model = Horarios
    context_object_name = 'horarios'
    template_name = 'horarios/horarios.html'

class CrearHorarios(CreateView):
    model = Horarios
    template_name = "horarios/crear_horario.html"
    form_class = HorariosForm
    success_url = reverse_lazy('horarios')

class EliminarHorarios(LoginRequiredMixin, DeleteView):
    model = Horarios
    template_name = "horarios/eliminar_horario.html"
    success_url = reverse_lazy('horarios')

class EditarHorarios(LoginRequiredMixin, UpdateView):
    model = Horarios
    template_name = "horarios/editar_horario.html"
    success_url = reverse_lazy('horarios')
    fields = ['horas_cargadas', 'tareas_realizadas', 'fecha_ingreso', 'imagen']

class DetalleHorarios(DetailView):
    model = Horarios
    template_name = "horarios/detalle_horario.html"



