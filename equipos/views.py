from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    TemplateView,
)
from .models import Equipo
# Create your views here.

class ListaEquipos(ListView):
    template_name = 'lista_equipos.html'
    model = Equipo
    paginate_by = 5
    context_object_name = 'lista_eq'

class CreaEquipos(CreateView):
    template_name = 'crea_equipo.html'
    model = Equipo
    #fields = ['nombre', 'nick', 'correo', 'password']
    fields = ('__all__')
    success_url = reverse_lazy('equipos_app:lista_equipos')