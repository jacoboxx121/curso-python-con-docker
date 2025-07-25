from flask import Flask, jsonify, request

from cliente import cliente 

app = Flask(__name__)

app.register_blueprint(cliente)

@app.route('/', methods=['GET'])

def entrada():    
    return "Bienvenido Usuario"

if __name__ == "__main__":
    app.run(debug=True, port=5003,host='0.0.0.0')
