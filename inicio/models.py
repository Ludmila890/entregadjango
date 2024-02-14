from django.db import models

class Empleados(models.Model):
    empleado = models.CharField(max_length=30)
    sector = models.CharField(max_length=30)
    jornada= models.IntegerField()
    
    def __str__(self):
        return f"{self.empleado} - {self.sector} - {self.jornada}"
    