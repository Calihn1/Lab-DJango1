from django import forms
from .models import Alumno, Curso, NotaAlumnoPorCurso

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre']