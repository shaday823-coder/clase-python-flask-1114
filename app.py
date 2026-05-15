# Importamos Flask y una funcion que permite mostrar un HTML.
from flask import Flask, render_template


# Creamos la aplicacion principal.
# Este objeto sera el centro de nuestro proyecto Flask.
app = Flask(__name__)


# Cuando alguien entra a la direccion principal del sitio, Flask ejecuta
# esta funcion y devuelve la pagina `index.html`.
@app.route("/")
def inicio():
    # `render_template` busca archivos dentro de la carpeta `templates`.
    return render_template("index.html")


@app.route("/HOLA")
def hola():
    # `render_template` busca archivos dentro de la carpeta `templates`.
    return render_template("HOLA.html")

@app.route("/ADIOS")
def adios():
    # `render_template` busca archivos dentro de la carpeta `templates`.
    return render_template("ADIOS.html")

@app.route("/LOVE")
def love():
    # `render_template` busca archivos dentro de la carpeta `templates`.
    return render_template("LOVE.html")


# Este bloque se ejecuta solo si corremos `python app.py` desde la terminal.
if __name__ == "__main__":
    # `debug=True` sirve en desarrollo porque reinicia el servidor
    # cuando detecta cambios y muestra errores con mas detalle.
    app.run(debug=True)
