from flask import Blueprint, render_template
from models.model import admin

pagina_simples = Blueprint('simple_page', __name__)

@pagina_simples.route('/', methods = ["POST"])
def mostrar():
    return render_template('index.html')

@pagina_simples.route('/', methods = ['POST'])
def pegar(): #o q eu to tentando desenvolver baseado no exemplo da prova do moodle q o igor falou pra eu ver ;-;
    

@pagina_simples.route('/usuario')
def mostrarUsuario():
    return render_template('index.html', usuario = admin)