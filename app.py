from flask import Flask, jsonify, render_template_string
import json

app = Flask(__name__)

# Ruta principal con HTML bonito
@app.route("/")
def home():
    html = """
    <html>
        <head>
            <title>🌐 Mi Web Service</title>
            <style>
                body { font-family: Arial; text-align: center; background: #f0f0f0; }
                h1 { color: #007BFF; }
                p { font-size: 18px; }
                .card {
                    background: white; 
                    padding: 20px; 
                    border-radius: 10px; 
                    width: 50%; 
                    margin: auto;
                    box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
                }
                a {
                    text-decoration: none;
                    color: white;
                    background: #007BFF;
                    padding: 10px 20px;
                    border-radius: 8px;
                    font-weight: bold;
                }
                a:hover {
                    background: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🚀 Bienvenido a mi Web Service Gratuito</h1>
                <p>Este servicio está hecho con Flask.</p>
                <p>
                    👉 Prueba la API con un clic:<br><br>
                    <a href="/api/saludo/Honorio%20Haro">Saludar a Honorio Haro</a>
                </p>
            </div>
        </body>
    </html>
    """
    return render_template_string(html)

# Endpoint JSON (API) con soporte de emojis y acentos
@app.route("/api/saludo/<nombre>")
def saludar(nombre):
    mensaje = {
        "saludo": f"Hola {nombre}, bienvenido a mi API con Flask 🎉 si ve esto póngame un diezon "
    }
    return app.response_class(
        response=json.dumps(mensaje, ensure_ascii=False),
        mimetype="application/json"
    )

# Iniciar servidor
if __name__ == "__main__":
    app.run(debug=True)
