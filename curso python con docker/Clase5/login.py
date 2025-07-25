# Importamos lo necesario de Flask para crear un grupo de rutas y manejar JSON/peticiones
from flask import Blueprint, Flask, jsonify, request

# Creamos un "bloque" (Blueprint) llamado "login" que agrupará todas las rutas de autenticación
login = Blueprint('login', __name__)

# Ruta POST "/login": cuando alguien llame a http://servidor/login con POST se ejecutará esta función
@login.route('/login', methods=['POST'])
def llamarServicioSet():
    # Extraemos del cuerpo de la petición (JSON) los valores enviados bajo las claves "user" y "password"
    user = request.json.get('user')
    password = request.json.get('password')

    # Mostramos en la consola del servidor los datos que llegaron para verificar
    print("User enviado:", user, "Pass enviado:", password)

    # Llamamos a una función auxiliar que validará usuario y contraseña
    # y devolverá 4 valores: código de resultado, mensaje, acción y rol
    codRes, menRes, accion, rol = inicializarVariables(user, password)

    # Armamos un diccionario con todos los datos que queremos devolver al cliente
    salida = {
        'codRes': codRes,   # Código de respuesta (SIN_ERROR o ERROR)
        'menRes': menRes,   # Mensaje descriptivo para el usuario
        'usuario': user,    # Usuario que intentó loguearse
        'accion': accion,   # Qué pasó con el login
        'rol': rol          # Rol asignado si el login fue exitoso
    }

    # Convertimos el diccionario en JSON y lo enviamos como respuesta HTTP
    return jsonify(salida)


# Función que recibe usuario y contraseña, los compara con los valores esperados
# y devuelve el resultado
def inicializarVariables(user, password):
    # Valores por defecto: todo está bien hasta que se demuestre lo contrario
    codRes = 'SIN_ERROR'
    menRes = "OK"
    accion = "Login exitoso"
    rol = "Admin"
    
    # Credenciales correctas almacenadas en el servidor
    userLocal = "derlisca"
    passwordLocal = "unida123"

    # Bloque try/except para capturar errores inesperados
    try:
        # Comparamos lo que llegó con lo que tenemos guardado
        if user == userLocal and password == passwordLocal:
            print("Login exitoso")  # Confirmamos en la consola del servidor
            accion = "Login exitoso"
        else:
            # Credenciales incorrectas: actualizamos los valores a retornar
            codRes = 'ERROR'
            menRes = "Usuario o contraseña incorrectos"
            accion = "Login fallido"
            rol = "N/A"
            user = "N/A"

    # Si ocurre cualquier error en el proceso (por ejemplo, que no llegue JSON)
    except Exception as e:
        print("Error en el login:", e)  # Mostramos en consola el error
        codRes = 'ERROR'
        menRes = "Error en el login"
        accion = "Error en el login"
        rol = "N/A"
        user = "N/A"
        # IMPORTANTE: esta línea sobra y nunca se ejecuta
        # return codRes, menRes, accion, rol, user
        # return codRes, menRes, accion,

    # Devolvemos los 4 valores a quien llamó a la función
    return codRes, menRes, accion, rol