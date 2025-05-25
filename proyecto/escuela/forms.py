from django import forms
from .models import Alumno, Curso, NotaAlumnoPorCurso

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre']

class NotaAlumnoPorCursoForm(forms.ModelForm):
    nombreCurso = forms.CharField(label='Nombre del curso')
    class Meta:
        model = NotaAlumnoPorCurso
        fields = ['nombreCurso', 'nota']

    def save(self, commit=True):
        nombre = self.cleaned_data['nombreCurso']
        curso, creado = Curso.objects.get_or_create(nombre=nombre)
        nota = super().save(commit=False)
        nota.curso = curso
        if commit:
            nota.save()
        return nota