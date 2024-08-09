Proyecto de web propia. Barra de navegacion funcional se va a dejar algo de informacion precargada

# Para la pre-entrega:
- Se usa la herencia de la barra de navegacion y el pie de pagina en la mayoria los archivos html.

- Tres clases de modelos:
  - Contact: Se usa el formulario de contacto que es funcional y guarda los datos en el administrador de django.
    - http://127.0.0.1:8000/contact/ 
  - Materiales: Se usa para agregar materiales de diferentes colores.
    -http://127.0.0.1:8000/materiales/  
  - Rating: Añade una opcion de calificaciones. 
    - http://127.0.0.1:8000/rate/
  - Users: Se importa el modelo de Users que trae django.
    - http://127.0.0.1:8000/register/ Registro de usuario. 
    - http://127.0.0.1:8000/login/ Login de usuario (Usuario: Test Pwd: 123).
  - Profile: Añade una imagen de perfil cuando el usuario esta logueado. 

- Formularios de busqueda:
  - Una vez agregados los materiales se pueden buscar en la pagina http://127.0.0.1:8000/materiales/
  - Si se registraron usuarios se pueden buscar en http://127.0.0.1:8000/search-email/
  - Se pueden ver las diferentes valoraciones de 1 a 5 estrellas http://127.0.0.1:8000/search_ratings/

Para probar:
- Colores ya cargados
  - verde
  - rojo
    
- Valoraciones ya hay de 1, 2, 3, 4 y 5 estrellas cargadas.

- Mail ya cargados a@b.com b@b.com

## TEMPLATE ORIGINAL https://startbootstrap.com/template/modern-business 
