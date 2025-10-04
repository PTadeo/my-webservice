from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensaje": "Bienvenido a mi API en Render 🚀"})

@app.route("/saludo", methods=["GET"])
def saludo():
    nombre = request.args.get("nombre", default="invitado")
    return jsonify({"mensaje": f"Hola {nombre}, bienvenido a mi API 🎉"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Render necesita host 0.0.0.0
