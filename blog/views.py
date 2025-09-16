from django.shortcuts import render, redirect
from .models import Juego
from .forms import JuegoForm, CategoriaForm, DesarrolladorForm, BusquedaJuegoForm

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def agregar_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JuegoForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Juego'})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Categoría'})

def agregar_desarrollador(request):
    if request.method == 'POST':
        form = DesarrolladorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DesarrolladorForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Desarrollador'})

def buscar_juego(request):
    resultados = []
    if request.method == 'POST':
        form = BusquedaJuegoForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultados = Juego.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaJuegoForm()
    return render(request, 'blog/buscar.html', {'form': form, 'resultados': resultados})
