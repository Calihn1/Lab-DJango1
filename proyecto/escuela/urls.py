from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaAlumnos, name='listaAlumnos'),
    path('alumno/nuevo/', views.agregarAlumno, name='agregarAlumno'),
    path('alumno/<int:alumno_id>/', views.detalleAlumno, name='detalleAlumno'),
    path('alumno/<int:alumno_id>/nueva-nota/', views.agregarNota, name='agregarNota'),
]