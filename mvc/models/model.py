class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        
lista = []
admin = Usuario("Pedro", "19")
lista.append(admin)
