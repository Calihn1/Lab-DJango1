from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno, NotaAlumnoPorCurso
from .forms import AlumnoForm, NotaAlumnoPorCursoForm

def listaAlumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'escuela/listaAlumnos.html', {'alumnos': alumnos})

