from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView
#from usuarios.views import ver_hobbies
#from usuarios.views import VerHobbiesView


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar', views.editar_perfil, name='editar_perfil'),
    path('perfil/editar/contrasenia', views.EditarContrasenia.as_view(), name='cambiar_contrasenia'),
    #path('ver-hobbies/', VerHobbiesView.as_view(), name='ver_hobbies')
]
