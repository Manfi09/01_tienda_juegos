# Tienda de Videojuegos

Proyecto Django que simula una tienda/blog de videojuegos. Cumple con:

- Arquitectura MVT (Modelo-Vista-Template)
- Herencia de plantillas con base.html
- 3 modelos principales (Videojuego, Desarrolladora, Plataforma)
- Formularios para creación y edición de modelos
- Búsqueda de videojuegos por título
- Sistema de autenticación con login, logout y registro
- Perfil de usuario con datos extendidos: nombre, apellido, email, avatar, biografía, fecha de cumpleaños, y más
- Edición de perfil y cambio de contraseña desde la vista de perfil
- Navegación responsive con Bootstrap 5.3 implementado en el navbar
- Control de acceso: vista principal bloqueada para usuarios no autenticados

## Cómo probar

1. Clonar el repo
2. Crear entorno virtual y activar
3. Instalar dependencias con `pip install -r requirements.txt`
4. Migrar la base de datos con `python manage.py migrate`
5. Correr el servidor con `python manage.py runserver`
6. Ir a [http://localhost:8000](http://localhost:8000)
7. Al entrar, serás redirigido a la página de login si no estás autenticado
8. Puedes registrarte o iniciar sesión para acceder a todas las funcionalidades
9. Desde el navbar podrás acceder a "Mi Perfil" para ver y editar tus datos, o cambiar tu contraseña

## Funcionalidades

- Crear, listar, buscar, editar y eliminar videojuegos, desarrolladoras y plataformas
- Registro, inicio y cierre de sesión de usuarios
- Perfil de usuario con avatar, biografía, fecha de cumpleaños, y más
- Edición de perfil y cambio de contraseña
- Navbar responsive y estilizado con Bootstrap 5.3
- Protección de rutas para usuarios autenticados

---

Si querés colaborar o sugerir mejoras, ¡bienvenido!  
Cualquier duda o problema, abrí un issue o contactame.

