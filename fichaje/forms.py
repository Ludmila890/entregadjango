from django import forms
from .models import Horarios

class HorariosForm(forms.ModelForm):
    class Meta:
        model = Horarios
        fields = ['horas_cargadas', 'tareas_realizadas', 'fecha_ingreso', 'imagen']
