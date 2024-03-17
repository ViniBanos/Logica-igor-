class Banco:
    def __init__(self, name, saldo, saldodevedor):
        self.name = name
        self.saldo = saldo
        self.saldodevedor = saldodevedor
        self.emp = None

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, sacar):
        if self.saldo > sacar:
            self.saldo = self.saldo - sacar
        else:
            print("Saldo insuficiente.")

    def emprestimo(self, emp, validade):
        self.emp = emp
        self.saldo = self.saldo + emp
        self.saldodevedor = ((emp * 0.01) * validade) + emp

    def mostrar_saldo(self):
        print(self.saldo)

    def mostrar_saldoneg(self):
        print(self.saldodevedor)
