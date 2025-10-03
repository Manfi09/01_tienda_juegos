from django.shortcuts import render, redirect
from django.contrib import messages  # Importamos el sistema de mensajes
from django.shortcuts import get_object_or_404  # Para buscar el juego de forma segura
from django.contrib.auth.forms import UserCreationForm  # Creacion de usuarios
from django.contrib.auth.decorators import login_required
from .models import Juego
from .forms import JuegoForm, CategoriaForm, DesarrolladorForm, BusquedaJuegoForm

# Create your views here.
@login_required
def home(request):
    return render(request, 'blog/home.html')

@login_required
def agregar_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Juego agregado correctamente ✅")
            return redirect('home')
        else:
            messages.error(request, "Hubo un error al agregar el juego. Revisa el formulario.")
    else:
        form = JuegoForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Juego'})

@login_required
def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Categoría'})

@login_required
def agregar_desarrollador(request):
    if request.method == 'POST':
        form = DesarrolladorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DesarrolladorForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Agregar Desarrollador'})

@login_required
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

@login_required
def borrar_juego(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    if request.method == 'POST':
        juego.delete()
        messages.success(request, "El juego ha sido eliminado ✅")
        return redirect('listar_juegos')  # Redirige a la lista
    return render(request, 'blog/confirmar_borrado.html', {'juego': juego})

@login_required
def listar_juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'blog/listar_juegos.html', {'juegos': juegos})

@login_required
def editar_juego(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    if request.method == 'POST':
        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            messages.success(request, "Juego actualizado correctamente ✏️")
            return redirect('detalle_juego', juego_id=juego.id)
    else:
        form = JuegoForm(instance=juego)
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Editar Juego'})

@login_required
def detalle_juego(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    return render(request, 'blog/detalle_juego.html', {'juego': juego})


@login_required
def about(request):
    return render(request, 'blog/about.html')


#Usuario
@login_required
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente. Ya podés iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})



