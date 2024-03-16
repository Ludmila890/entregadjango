from django.urls import path
from fichaje import views

urlpatterns = [
    path('horarios/', views.ListarHorarios.as_view(), name='horarios'),
    path('horarios/nuevo/', views.CrearHorarios.as_view(), name='crear_horario'),
    path('horarios/<int:pk>/', views.DetalleHorarios.as_view(), name='detalle_horario'), 
    path('horarios/<int:pk>/editar/',views.EditarHorarios.as_view(), name='editar_horario'), 
    path('horarios/<int:pk>/eliminar/', views.EliminarHorarios.as_view(), name='eliminar_horario')
]
