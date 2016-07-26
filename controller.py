# Script para el control de las direcciones del servidor 
# Autor: Diego García Pérez 
# Descripción: Con la ayuda de flask asignaremos las direcciones a una funcion, 
# 				controlando el flujo de las 


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('view.html')

@app.route('/hola', methods=['GET', 'POST'])
def hola():

    return 'hola'

if __name__ == '__main__':
    app.run(debug=True)