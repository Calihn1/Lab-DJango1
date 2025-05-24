from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    def __str__(self):
        return self.nombre
    
class NotaAlumnoPorCurso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2)
