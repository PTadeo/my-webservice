from flask import Flask, jsonify, render_template_string
import json

# 1. Crear la aplicación
app = Flask(__name__)

# 2. Rutas
@app.route("/")
def home():
    return "Hola, este es el home"

@app.route("/api/saludo/<nombre>")
def saludar_api(nombre):
    mensaje = {"saludo": f"Hola {nombre}"}
    return app.response_class(
        response=json.dumps(mensaje, ensure_ascii=False, indent=4),
        mimetype="application/json"
    )

@app.route("/web/saludo/<nombre>")
def saludar_web(nombre):
    return f"<h1>👋 Hola {nombre}!</h1><p>Bienvenido a mi API con Flask 🎉</p>"

# 3. Ejecutar (solo localmente, Render no usa esto)
if __name__ == "__main__":
    app.run(debug=True)

