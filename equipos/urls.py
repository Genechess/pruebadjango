from django.urls import path
from . import views

app_name = 'equipos_app'

urlpatterns = [
    path('lista-equipos/', views.ListaEquipos.as_view(), name='lista_equipos'),
    path('alta-equipo/', views.CreaEquipos.as_view(), name='alta'),
]