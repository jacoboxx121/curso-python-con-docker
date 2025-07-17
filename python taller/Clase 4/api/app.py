#-*- Coding utf-8 -*-
#caracteres especiales


from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods=['GET'])

def unida():
    return "Hola desde la unida!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)