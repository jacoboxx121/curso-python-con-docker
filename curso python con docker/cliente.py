from flask import Blueprint, Flask, jsonify, request

cliente = Blueprint('cliente', __name__ )

app = Flask(__name__)


@cliente.route('/cliente', methods=['POST'])

def llamarServicioSet():
    nombre = request.json.get('nombre')
    ci = request.json.get('ci')

    print("nombre enviado:",nombre,"Cedula enviada:",ci)

    codRes,menRes,accion =inicializar_Variables(nombre,ci)

    salida ={
        "codRes":codRes, 
        "menRes":menRes,
        "accion":accion,
        "nombre":nombre,
        "cedula":ci
    }
    return jsonify(salida)

def inicializar_Variables(nombre, ci):
    accion = "Success"
    codRes = 'SIN_ERROR'
    menRes = "OK"

    nombre_local ="jacobo"
    ci_local= "5767495"
    
    try:
        if nombre == nombre_local and ci == ci_local:
         print("Usuario Correcto")

         accion ="Success"
        else:
            accion = "Cliente no existe"
            codRes = 'ERROR'
            menRes = "Error cliente"
            ci = "5767596"  
    except Exception as e:
     print("Error en el login:", e) 
     codRes = 'ERROR'
     menRes = "Error en el login"
     accion = "Error en el login"
    return codRes, menRes, accion