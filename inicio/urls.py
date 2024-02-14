
from django.urls import path
from inicio.views import inicio, lista_empleados, crear_empleado


urlpatterns = [
    path('',inicio,name='inicio'),
    path('crear-empleado/<str:empleado>/<str:sector>/<int:jornada>/',crear_empleado,name='crear_empleado'),
    #path('empleados/nuevo/<str:empleado>/<str:sector>/<int:jornada>/',crear_empleado,name='crear_empleado'),
    path('lista_empleados/', lista_empleados,name='lista_empleados'),
    path('empleados/nuevo/', crear_empleado,name='crear_empleado'),
    
]
