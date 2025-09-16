from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Desarrollador(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    desarrollador = models.ForeignKey(Desarrollador, on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField()

    def __str__(self):
        return self.titulo


