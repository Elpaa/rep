from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('detalle_paciente/<int:paciente_id>/', views.detalle_paciente, name='detalle_paciente'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/<int:usuario_id>/', views.detalle_usuario, name='detalle_usuario'),
    path('crear_paciente/', views.crear_paciente, name='crear_paciente'),
    path('editar_paciente/<int:paciente_id>/', views.editar_paciente, name='editar_paciente'),
    path('eliminar_paciente/<int:paciente_id>/', views.eliminar_paciente, name='eliminar_paciente'),
    path('crear_llamada_paciente/', views.crear_llamada_paciente, name='crear_llamada_paciente'),
    path('lista_llamadas_pacientes/', views.lista_llamadas_pacientes, name='lista_llamadas_pacientes'),
    path('detalle_llamada_paciente/<int:llamada_id>/', views.detalle_llamada_paciente, name='detalle_llamada_paciente'),
    path('registro/', views.register_user, name='registro'),
    path('login/', views.login_user, name='login'), 
    path('perfil/', views.perfil, name='perfil'),
]