from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo = models.CharField(max_length=100)
    nombre = models.TextField()
    creditos = models.IntegerField()  # Duración en horas

