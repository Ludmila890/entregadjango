from django import forms

class formularioCreacionEmpleados(forms.Form):
    
    empleado = forms.CharField(max_length=30)
    sector = forms.CharField(max_length=30)
    jornada= forms.IntegerField()
    