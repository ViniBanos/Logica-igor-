from flask import Flask, render_template, session, request, redirect, url_for
from controllers.login_controller import pagina_simples


app = Flask(__name__)
app.secret_key = 'chave_secreta'
app.register_blueprint(pagina_simples)

@app.errorhandler(404)
def error404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error500(e):
    return render_template('500.html'), 500


@app.errorhandler(401)
def error401(e):
    return render_template('401.html'), 401

if __name__ == '__main__':
    app.run(debug=True)
