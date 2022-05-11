from django.db import models

# Create your models here.
class Equipo(models.Model):
    conferencias = (
        ('AFC', 'American'),
        ('NFC', 'National'),
    )

    divisiones = (
        ('East','East'),
        ('West','West'),
        ('South','South'),
        ('North','North'),
    )

    nombre = models.CharField("Equipo", max_length=30)
    nombre_corto = models.CharField("Equ", max_length=4)
    conferencia = models.CharField("Conferencia", max_length=8, choices = conferencias, default = 'NFC')
    division = models.CharField("Div", max_length=5, choices = divisiones, default = 'East')
    ganados = models.IntegerField("W", default=0)
    perdidos = models.IntegerField("L", default=0)
    empatados = models.IntegerField("T", default=0)
    logo = models.ImageField("Logo", blank=True, upload_to='img/equipo')
 
    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['conferencia','division']

    def __str__(self):
        return self.nombre + '(' + str(self.ganados) + '-' + str(self.perdidos) + '-' + str(self.empatados) + ')'