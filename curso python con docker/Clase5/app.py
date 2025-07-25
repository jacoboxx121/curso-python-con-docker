# -*- coding: utf-8 -*-
# Le dice a Python que el archivo usa caracteres especiales (tildes, ñ, etc.)

# Importamos la librería "Flask" y algunas de sus funciones
from flask import Flask, jsonify, request

# Traemos el grupo de rutas "login" desde otro archivo llamado login.py
from login import login

# Traemos el grupo de rutas "logout" desde otro archivo llamado logout.py
from logout import logout

# Creamos la aplicación de Flask (será nuestro servidor web)
app = Flask(__name__)

# Agregamos las rutas de "login" al servidor
app.register_blueprint(login)

# Agregamos las rutas de "logout" al servidor
app.register_blueprint(logout)

# Definimos la dirección o "ruta" principal "/" y permitimos que solo se use con GET
@app.route('/', methods=['GET'])
def unida():
    # Cuando alguien visite la página principal, devolvemos este texto
    return 'Server Flask is running on port 5000!'

# Esta línea solo se ejecuta si abrimos este archivo directamente (no si lo importamos)
if __name__ == '__main__':
    # Arrancamos el servidor:
    # - debug=True: muestra errores detallados y reinicia automáticamente al cambiar el código
    # - port=5000: el servidor escucha en el puerto 5000
    # - host='0.0.0.0': permite que cualquier dispositivo de la red local se conecte
    app.run(debug=True, port=5000, host='0.0.0.0')

'''
0.0.0.0 es una dirección IP que permite que la aplicación Flask sea accesible desde cualquier dirección IP en la red local. 
'''