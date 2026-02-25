from flask import Flask
app = Flask(__name__)
#ruta principal
@app.route('/')
def index():
    return "Hola Mundo"
#ruta con parametro
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"Bienvenido estas en mi clase, {nombre}"

if __name__ == '__main__':
    app.run(debug=True)