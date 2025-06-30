from django.db import models

# Create your models here.
class Estudiante(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.TextField()
    apellidos = models.TextField()
    fecha_nacimiento = models.DateField()
    foto =models.ImageField(upload_to='estudiantes', null=True, blank=True)