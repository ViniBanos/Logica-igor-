from flask import Flask, render_template, redirect, url_for, abort, session, request, make_response
from controllers.login_controller import pagina_simples


app = Flask(__name__)
app.secret_key = 'chave_secreta'

#middleware de cria 
rotas_publicas = ["pagina_simples.login", "pagina_simples.home"]
rotas_adm = ['pagina_simples.admin']
@pagina_simples.before_request
def verificarlog(): 
    rota = request.endpoint
    if rota in rotas_publicas or rota is None:
        if rota == "pagina_simples.login" and 'idUser' in session:
            return redirect(url_for("pagina_simples.home"))
        return
    if 'idUser' not in session: 
        abort(401)
    if rota in rotas_adm:
        if session.get('idUser') != 1:
            abort(403)

app.register_blueprint(pagina_simples)



@app.errorhandler(404)
def error404(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def error403(e):
    return render_template('403.html'), 403


@app.errorhandler(401)
def error401(e):
    return render_template('401.html'), 401

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/set_cookie')
def set_cookie():
    resp = make_response('Cookie has been set')
    resp.set_cookie('name', 'Igor', max_age=60*60*24)

@app.route('/get_cookie')
def get_cookie():
    nome = request.cookies.get('name')
    if nome:
        return f'O nome é {nome}'
    else:
        return 'Não achei o cookie'
    
@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response('Cookie foi deletado!')
    resp.set_cookie('name', '', expires=0 )
    return resp