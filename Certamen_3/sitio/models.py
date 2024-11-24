from django.db import models

# Create your models here.
class Institucion(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nombre}'

class Tipo(models.Model):
    nombre=models.TextField(blank=True)

    def __str__(self):
        return f'{self.nombre}'
    
class EventoAcademico(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name='events')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    tipo_evento = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='events')  # e.g., 'exam', 'period_start', 'application_deadline'

    def __str__(self):
        return f'{self.titulo}'


class Feriado(models.Model):
    fecha = models.DateField()
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f'{self.nombre}'