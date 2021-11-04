


from flask import Flask
import os
from flask import request
from jose import jwt

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World Tokens!</p>"


@app.route("/crear-token")
def crear():
    nombre = request.args.get("nombre")
    id_persona = request.args.get("id")
    id_rol = request.args.get("id_rol")
    try:

        token = jwt.encode({'nombre': nombre, 'id': id_persona, 'rol': id_rol}, "ASJDFASDIDASJFASFJKL", algorithm='HS256')
        return token
    except Exception as e:
        return ""

@app.route("/validar-token")
def validar():
    token = request.args.get("token")
    rol = request.args.get("rol")
    try:
        token = jwt.decode(token, "ASJDFASDIDASJFASFJKL", algorithms=['HS256'])
        if token["rol"] == rol:
            return "OK"
        else:
            return "KO"
    except Exception as e:
        return ""
if __name__ == '__main__':
    app.run(host="localhost", port=5001)
