from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta que recibe un parámetro por la URL
@app.route("/saludo", methods=["GET"])
def saludo():
    # Obtener el parámetro "nombre" desde la URL ?nombre=valor
    nombre = request.args.get("nombre", default="invitado")

    # Usar el parámetro en la respuesta JSON
    respuesta = {
        "mensaje": f"Hola {nombre}, bienvenido a mi API 🎉",
        "status": "ok"
    }

    return jsonify(respuesta)

if __name__ == "__main__":
    app.run(debug=True)
