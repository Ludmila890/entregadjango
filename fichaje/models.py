from django.db import models

class Horarios(models.Model):
    horas_cargadas = models.CharField(max_length=30)
    tareas_realizadas= models.CharField(max_length=30)
    fecha_ingreso= models.DateField()
    
    def __str__(self):
        return f"{self.horas_cargadas} - {self.tareas_realizadas} "
    
