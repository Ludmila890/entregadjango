from django.db import models

class Horarios(models.Model):
    horas_cargadas = models.CharField(max_length=30)
    tareas_realizadas= models.CharField(max_length=30)
    fecha_ingreso= models.DateField()
    imagen = models.ImageField(upload_to='imagen', null=True, blank=True)  # Campo de imagen
    
    def __str__(self):
        return f"{self.horas_cargadas} - {self.tareas_realizadas}"
    
