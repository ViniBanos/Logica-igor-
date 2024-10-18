from flask import Flask, render_template, session, request, redirect, url_for
from controllers.controller import pagina_simples

app = Flask(__name__)
app.secret_key = 'chave_secreta'
app.register_blueprint(pagina_simples)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/login', methods = ['POST', 'GET'])
def login ():
    if request.method == 'POST':
        session ['name'] = request.form['name']
        return redirect(url_for ('hello'))
    return  

if __name__ == '__main__':
    app.run(debug=True)
