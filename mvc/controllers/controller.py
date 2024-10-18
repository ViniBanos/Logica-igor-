from flask import Blueprint, render_template, request
from models.model import Usuario, lista

pagina_simples = Blueprint('simple_page', __name__)

@pagina_simples.route('/')
def mostrar():
    return render_template('index.html')

@pagina_simples.route('/login', methods = ['POST'])
def pegar():
    name = request.form["name"]
    senha = request.form["senha"]
    for pessoa in lista:
        if name == pessoa.nome:
            if senha == pessoa.senha:
                return 'Logado Games'
    return 'Não logado Games'
