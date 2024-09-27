from flask import Flask
from controllers.controller import pagina_simples

app = Flask(__name__)
app.register_blueprint(pagina_simples)

@app.route("/")
def hello():
    return "Hello Word!"

if __name__ == '__main__':
    app.run(debug=True)