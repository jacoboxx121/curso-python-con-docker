# -*- coding: utf-8 -*-
# Indica a Python que el archivo puede contener letras especiales como tildes o la ñ.

# Importamos Flask (para crear el servidor web) y jsonify/request
# (aunque no se usan en este ejemplo, se suelen importar de costumbre).
from flask import Flask, jsonify, request

# Creamos la aplicación (servidor) de Flask.
app = Flask(__name__)

# Definimos la ruta "/" (la página principal) y decimos que solo acepte peticiones GET.
@app.route('/', methods=['GET'])
def unida():
    # Cuando alguien acceda a la página, le devolvemos el texto "Hola desde la Unida".
    return 'Hola desde la Unida'

# Si ejecutamos este archivo directamente (no lo usamos como módulo)...
if __name__ == '__main__':
    # ...ponemos en marcha el servidor:
    #   - debug=True: muestra errores detallados y recarga automáticamente al guardar cambios.
    #   - port=5000: escucha en el puerto 5000.
    #   - host='0.0.0.0': permite que cualquier dispositivo de la red local se conecte.
        app.run(debug=True, port=5000, host='0.0.0.0')

'''
0.0.0.0 es una dirección IP que permite que la aplicación Flask sea accesible desde cualquier dirección IP en la red local. 
'''