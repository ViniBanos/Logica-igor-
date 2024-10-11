class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
admin = Usuario("Pedro", 19)
u =  Usuario()
lista = [admin]
lista.append(u)