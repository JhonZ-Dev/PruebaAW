#importar la libreria flask
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates') #Creamos una variable de tipo app y pedimos a la funcion Flask


@app.route('/')
# llamar a index.html en la ruta principal
def principal():
    return render_template('/index.html')

# @app.route('/tienda')
# # llamar a index.html en la ruta principal
# def principal():
#     return render_template('/tienda.html')
# # ejecutar

@app.route('/tienda')
# llamar a contacto.html a la ruta seucndaria
def login():
    return render_template('/tienda.html')

@app.route('/historial')
# llamar a contacto.html a la ruta seucndaria
def historial():
     return render_template('/historial.html')


if __name__ == '__main__':
    app.run(debug=True)
