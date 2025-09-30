@app.route("/web/saludo/<nombre>")
def saludar_web(nombre):
    return render_template_string(f"""
    <html>
        <head>
            <title>Saludo Web</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: #f4f4f9;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }}
                .card {{
                    background: white;
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                    text-align: center;
                }}
                h1 {{ color: #007BFF; }}
                p {{ color: #555; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>👋 Hola {nombre}!</h1>
                <p>Bienvenido a mi API con Flask 🎉</p>
                <p>Desarrollado por <b>Pablo Tadeo Torres Leal</b></p>
            </div>
        </body>
    </html>
    """)
