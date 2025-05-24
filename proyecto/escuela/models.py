from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    def __str__(self):
        return self.nombre
