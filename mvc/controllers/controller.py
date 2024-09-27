from flask import Blueprint, render_template
from models.model import skyline

pagina_simples = Blueprint('simple_page', __name__)

@pagina_simples.route('/')
def mostrar():
    return render_template('index.html')

@pagina_simples.route('/carro')
def mostrarCarro():
    return render_template('index.html', carro = skyline)