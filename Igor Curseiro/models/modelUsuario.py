class Usuario:
    def __init__(self, nome, senha, id):
        self.nome = nome
        self.senha = senha
        self.id = id 
        
usuarios = []
pedro = Usuario("Pedro", "19", "1")
usuarios.append(pedro)
