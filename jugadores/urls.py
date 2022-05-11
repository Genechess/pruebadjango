from django.urls import path
from . import views

app_name = 'jugadores_app'

urlpatterns = [
    path('lista-jugadores/', views.ListaJugadores.as_view(), name='todos_los_jugadores'),
    path('lista-jugadores-admin/', views.ListaJugadoresAdmin.as_view(), name='jugadores_admin'),
    path('Lista-JugadoresXEq/<parametro>', views.ListaJugadoresXEquipo.as_view(), name='jugadores-x-equipo'),
    path('Lista-JugadoresXKey/', views.ListaJugadoresXKey.as_view()),
    path('jugador-detalle/<pk>', views.JugadoresDetalle.as_view(), name='detalle_jugador'),
    path('alta-jugador/', views.CreaJugadores.as_view(),name='alta'),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('actualizar-jugador/<pk>', views.ActualizaJugadores.as_view(), name='actualizar'),
    path('eliminar-jugador/<pk>', views.EliminaJugadores.as_view(), name='borrar'),
    path('alta-jugador-form/', views.CreaJugadoresForm.as_view(), name='crearjugadoresform'),
    path('jugador-equipo-form/', views.Jugador_Equipo_View.as_view(), name = 'jugadorequipoform'),
    path('', views.HomeView.as_view(), name = 'home'),
]