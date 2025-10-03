"""
URL configuration for blog_juegos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('juego/', views.agregar_juego, name='agregar_juego'),
    path('categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('desarrollador/', views.agregar_desarrollador, name='agregar_desarrollador'),
    path('buscar/', views.buscar_juego, name='buscar_juego'),
    path('about/', views.about, name='about'),
    path('juegos/', views.listar_juegos, name='listar_juegos'),
    path('juego/<int:juego_id>/', views.detalle_juego, name='detalle_juego'),
    path('juego/editar/<int:juego_id>/', views.editar_juego, name='editar_juego'),
    path('juego/borrar/<int:juego_id>/', views.borrar_juego, name='borrar_juego'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('blog.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)