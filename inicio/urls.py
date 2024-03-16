
from django.urls import path
from inicio.views import inicio, about, crear_empleado, lista_empleados,  ver_empleados, eliminar_empleados, editar_empleados

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about', about, name='about'),
    path('crear-empleado/<str:empleado>/<str:sector>/<int:jornada>/', crear_empleado, name='crear_empleado'),
    path('lista_empleados/nuevo/', crear_empleado, name='crear_empleado'),
    path('lista_empleados/', lista_empleados, name='lista_empleados'),
    path('lista_empleados/<int:id_empleado>/', ver_empleados, name='ver_empleado'),
    path('lista_empleados/<int:id_empleado>', ver_empleados, name='ver_empleado'),
    path('lista_empleados/<int:id_empleado>/eliminar/', eliminar_empleados, name='eliminar_empleado'),
    path('lista_empleados/<int:id_empleado>/editar/', editar_empleados, name='editar_empleado'),
    
]

