from django import forms
from .models import Juego, Categoria, Desarrollador

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class DesarrolladorForm(forms.ModelForm):
    class Meta:
        model = Desarrollador
        fields = '__all__'

class BusquedaJuegoForm(forms.Form):
    titulo = forms.CharField(label="Buscar juego por título", max_length=100)
