# Importamos lo necesario de Flask: Blueprint (para crear un grupo de rutas),
# Flask (aunque no se usa aquí, se importa por costumbre), jsonify (para devolver JSON)
# y request (para leer lo que nos envía el cliente).
from flask import Blueprint, Flask, jsonify, request

# Creamos un nuevo "bloque" o conjunto de rutas llamado "logout".
# Así luego podremos añadirlo a la aplicación principal.
logout = Blueprint('logout', __name__)

# Definimos la ruta "/logout" que solo acepta peticiones HTTP de tipo POST.
@logout.route('/logout', methods=['POST'])
def llamarServicioSet():
    # Extraemos del cuerpo de la petición (formato JSON) el valor que viene bajo la clave "user".
    user = request.json.get('user')
    
    # Extraemos del cuerpo de la petición el valor que viene bajo la clave "password".
    password = request.json.get('password')
    
    # Imprimimos en la consola del servidor los valores que acabamos de recibir.
    # Esto sirve para verificar que llegan correctamente.
    print("User enviado:", user, "Pass enviado:", password)

    # (Nota: esta función no devuelve nada al cliente, por eso no hay return.
    #        En producción debería enviarse una respuesta.)