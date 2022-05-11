from django import forms
from .models import Jugador

class JugadorForm(forms.ModelForm):

    class Meta:
        model = Jugador
        fields = ('__all__')

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese el nombre del jugador aquí'
                }
            )
        }

    def clean_nick(self):
        data = self.cleaned_data["nick"]
        if len(data) < 6:
            raise forms.ValidationError('El apodo debe tener al menos 6 caracteres')
        return data

class Jugador_Equipo_Form(forms.Form):
    nombre = forms.CharField(max_length=60)
    nick = forms.CharField(max_length=60)
    correo = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60)
    equipo = forms.CharField(max_length=60)
    eq = forms.CharField(max_length=60)
    
        