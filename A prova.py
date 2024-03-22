class Funcionario:
    def __init__(self, nome: str, salario_base: float):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        salfinal = self.salario_base
        return f'O seu salário final é: {salfinal}'


class FuncionarioRegular(Funcionario):
    def __init__(self, nome: str, salario_base: float):
        super().__init__(nome, salario_base)

    def calcular_salario(self):
        salfinal = self.salario_base
        return f'O seu salário final é: {salfinal}'


class Gerente(Funcionario):
    def __init__(self, nome: str, salario_base: float, bonus: float):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        salfinal = self.salario_base + self.bonus
        return f'O seu salário final é: {salfinal}'
        

class Diretor(Funcionario):
    def __init__(self, nome: str, salario_base: float, participacao_lucros: float):
        super().__init__(nome, salario_base)
        __self.participacao_lucros = participacao_lucros
    
    def calcular_salario(self):
        salfinal = self.salario_base + self.participacao_lucros
        return f'O seu salário final é: {salfinal}'


def calcular_folha_pagamento(lista_funcionarios: list):
    total = 0
    for salario in lista_funcionarios:
        total += lista_funcionarios[salario]
    print(f'Total pago em salários: R${total:.2f}')
        
gerente = Gerente('Nilto', 1500, 500)
gerente.calcular_salario()

funcA = Funcionario('Roberto', 1)
funcB = Funcionario('Daniel', 1)

calcular_folha_pagamento([funcA, funcB])
