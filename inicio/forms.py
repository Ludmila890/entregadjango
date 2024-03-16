from django import forms


...
class formularioBaseEmpleados(forms.Form):
    empleado = forms.CharField(max_length=30)
    sector = forms.CharField(max_length=30)
    jornada= forms.IntegerField()
    
...
class formularioCreacionEmpleados(formularioBaseEmpleados):
    
    ...
    
...
class formularioEdicionEmpleados(formularioBaseEmpleados):
    jornada= forms.IntegerField()
    
...
class BusquedaEmpleado(forms.Form):
    empleado = forms.CharField(max_length=30)