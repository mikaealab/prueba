from django.urls import path
from . import views

urlpatterns = [
    path('', views.estudiantes, name='estudiantes'),
    path('listadoEstudiantes', views.listadoEstudiantes, name='listadoEstudiantes'),
    path('nuevoEstudiante/', views.nuevoEstudiante, name='nuevoEstudiante'),
    path('editarEstudiante/<int:id>/', views.editarEstudiante, name='editarEstudiante'),
    path('eliminarEstudiante/<int:id>/', views.eliminarEstudiante, name='eliminarEstudiante'),
]
