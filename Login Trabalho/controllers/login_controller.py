from flask import Blueprint, render_template, request, url_for, redirect, session, flash, abort, make_response
from models.modelUsuario import Usuario, usuarios

pagina_simples = Blueprint('pagina_simples', __name__)

rodando = True
@pagina_simples.route('/')
def home():
    global rodando
    if rodando:
        session.clear()
        rodando = False
    if 'idUser' in session: #coloquei idUser pq acredito eu que não faz diferença, e é até melhor. Mas não entendi pq está dando erro com o 'nome'. to a 3 horas nisso. 
        return f'Bem Vindo(a) {session["nome"]}!'
    return render_template('index.html')

@pagina_simples.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        nome = request.form["name"]
        senha = request.form["senha"]
        for pessoa in usuarios:
            if nome == pessoa.nome:
                if senha == pessoa.senha:
                    session ['idUser'] = pessoa.id
                    session ['nome'] = pessoa.nome
                    rodando = 1
                    flash("Bem vindo do flash massage! ", "success")
                    return redirect(url_for("pagina_simples.dashboard"))
                flash("Nome Correto, senha errada", "error")
                return redirect(url_for("pagina_simples.login"))
            flash("Nome errado, senha errada", "error")
        return redirect(url_for('pagina_simples.login'))
    return render_template('login.html')
    
@pagina_simples.route('/dashboard')
def dashboard():
    return render_template("dash.html")

@pagina_simples.route('/logout')
def logout():
    session.pop('idUser', None)
    return redirect(url_for('pagina_simples.home'))
    
@pagina_simples.route('/admin')
def admin():
    if session.get('idUser') != 1:
        abort(403)
    return render_template("admin.html")