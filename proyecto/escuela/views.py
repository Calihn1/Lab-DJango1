from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno, NotaAlumnoPorCurso
from .forms import AlumnoForm, NotaAlumnoPorCursoForm

def listaAlumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'escuela/listaAlumnos.html', {'alumnos': alumnos})

def agregarAlumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaAlumnos')
    else:
        form = AlumnoForm()
    return render(request, 'escuela/formulario.html', {'form': form, 'titulo': 'Agregar Alumno'})

def detalleAlumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)
    notas = NotaAlumnoPorCurso.objects.filter(alumno=alumno)
    return render(request, 'escuela/detalleAlumno.html', {'alumno': alumno, 'notas': notas})

