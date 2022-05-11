#from attr import fields
from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Jugador
from equipos.models import Equipo
from .forms import Jugador_Equipo_Form, JugadorForm
from django.views.generic.edit import FormView
# Create your views here.

#Vista Home
class HomeView(TemplateView):
    template_name = 'home.html'

class Jugador_Equipo_View(FormView):
    template_name = 'form_jugador_equipo.html'
    form_class = Jugador_Equipo_Form
    success_url = reverse_lazy('jugadores_app:correcto')

    def form_valid(self, form):
        nombres = form.cleaned_data['nombre']
        nick = form.cleaned_data['nick']
        correo = form.cleaned_data['correo']
        password = form.cleaned_data['password']
        equipo = form.cleaned_data['equipo']
        eq = form.cleaned_data['eq']
        equipo_model = Equipo(
            nombre = form.cleaned_data['equipo'],
            nombre_corto = form.cleaned_data['eq'],
            conferencia = 'National',
            division = 'South'
        )
        equipo_model.save()
        Jugador.objects.create(
            nombre = nombres,
            nick = nick,
            correo = correo,
            password = password,
            equipo = equipo_model
        )
        return super().form_valid(form)

class CreaJugadoresForm(CreateView):
    template_name = 'form_crea_jugadores.html'
    model = Jugador
    form_class = JugadorForm
    success_url = reverse_lazy('jugadores_app:correcto')

    def form_valid(self, form):
        jugador = form.save()
        jugador.nombre = jugador.nombre + ' ' + jugador.nick
        jugador.save()
        return super().form_valid(form)

class EliminaJugadores(DeleteView):
    template_name = 'elimina_jugadores.html'
    model = Jugador
    context_object_name = 'vista'
    #fields = ['nombre', 'nick', 'correo', 'password']
    fields = ('__all__')
    success_url = reverse_lazy('jugadores_app:jugadores_admin')

class ActualizaJugadores(UpdateView):
    template_name = 'actualiza_jugadores.html'
    model = Jugador
    #fields = ['nombre', 'nick', 'correo', 'password']
    fields = ('__all__')
    success_url = reverse_lazy('jugadores_app:jugadores_admin')

    def post(self, request, *args, **kwargs):
        #Primero se ejecuta el POST, después se valida el FORM
        print (request.POST['nombre'] + ' se ha actuazlizado!')
        return super().post(request, *args, **kwargs)

class SuccessView(TemplateView):
    template_name = 'success.html'

class CreaJugadores(CreateView):
    template_name = 'crea_jugadores.html'
    model = Jugador
    #fields = ['nombre', 'nick', 'correo', 'password']
    fields = ('__all__')
    success_url = reverse_lazy('jugadores_app:todos_los_jugadores')

    def form_valid(self, form):
        jugador = form.save()
        jugador.nombre = jugador.nombre + ' ' + jugador.nick
        jugador.save()
        return super().form_valid(form)

class ListaJugadores(ListView):
    template_name = 'lista_jugadores.html'
    context_object_name = 'lista_ju'
    paginate_by = 5
    ordering = 'nick'

    def get_queryset(self):
        parametro = self.request.GET.get('buscar', '')
        resultado = Jugador.objects.filter(
            nombre__icontains = parametro
        )
        return resultado

class ListaJugadoresXEquipo(ListView):
    template_name = 'lista_jugadores_eq.html'
    model = Jugador
    #queryset = Jugador.objects.filter(
    #    equipo__nombre_corto='PIT'
    #)
    context_object_name = 'lista_ju_x_eq'


    def get_queryset(self):
        parametro = self.kwargs['parametro']
        resultado = Jugador.objects.filter(
            equipo__nombre_corto = parametro
        )
        return resultado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipo_param'] = self.kwargs['parametro']
        print ('               PARAM: ')
        return  context


class ListaJugadoresXKey(ListView):
    model = Jugador
    template_name = 'lista_jugadores_key.html'
    #queryset = Jugador.objects.filter(
    #    equipo__nombre_corto='PIT'
    #)
    context_object_name = 'lista_ju_x_key'


    def get_queryset(self):
        parametro = self.request.GET.get('keyw', '')
        resultado = Jugador.objects.filter(
            equipo__nombre_corto = parametro
        )
        return resultado

class JugadoresDetalle(DetailView):
    template_name = 'jugador_detalle.html'
    model = Jugador
    context_object_name = 'jugador_detalle'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_param'] = 'detalle'
        return  context

class ListaJugadoresAdmin(ListView):
    template_name = 'lista_jugadores_admin.html'
    context_object_name = 'lista_ju'
    paginate_by = 5
    ordering = 'nick'
    model = Jugador

    def get_queryset(self):
        parametro = self.request.GET.get('buscar', '')
        resultado = Jugador.objects.filter(
            nombre__icontains = parametro
        )
        return resultado