from flask import Blueprint, render_template, request, url_for, redirect, session, flash, abort 
from models.modelUsuario import Usuario, usuarios

pagina_simples = Blueprint('pagina_simples', __name__)

@pagina_simples.route('/')
def home():
    return render_template('index.html')

@pagina_simples.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form["name"]
        senha = request.form["senha"]
        for pessoa in usuarios:
            if name == pessoa.nome:
                if senha == pessoa.senha:
                    session ['idUser'] = pessoa.id
                return redirect(url_for("pagina_simples.dashboard"))
        return redirect(url_for('pagina_simples.login'))
    return render_template('login.html')
    
@pagina_simples.route('/dashboard')
def dashboard():
    return render_template("dash.html")

@pagina_simples.route('/logout')
def logout():
    session.pop('idUser', None)
    return redirect(url_for('pagina_simples.home'))

#middleware de cria 
rotas_publicas = ["pagina_simples.login", "pagina_simples.home"]
@pagina_simples.before_request
def verificarlog(): 
    if request.endpoint in rotas_publicas:
        return

    if 'idUser' not in session:
        return redirect(url_for("pagina_simples.login"))
    
@pagina_simples.route('/admin')
def admin():
    if session.get('idUser') != 1:
        abort(401)
    return render_template("admin.html")