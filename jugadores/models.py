from mailbox import Maildir
from tkinter import HIDDEN
from tokenize import Ignore
from django.db import models
from equipos.models import Equipo

# Create your models here.
class Jugador(models.Model):
    nombre = models.CharField("Nombre", max_length=70)
    nick = models.CharField("Apodo", max_length=30)
    correo = models.EmailField("Correo", max_length=254)
    password = models.CharField("password",max_length=20)
    equipo = models.ForeignKey(Equipo, verbose_name=("Equipo"), on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        ordering = ['nick']

    def __str__(self):
        return str(self.id) + '.- ' + self.nick