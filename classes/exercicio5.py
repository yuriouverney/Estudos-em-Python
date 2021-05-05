'''Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
com valor default zero e os demais atributos são obrigatórios.'''

class Conta:
    def __init__(self, numero, nome, saldo = 0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, nome_nome):
        self.nome = nome
        return self.nome

    def deposito(self, valor_deposito):
        self.saldo = valor_deposito
        return self.saldo

    def saque(self, valor_saque):
        self.saque = valor_saque
        return self.saldo

c = Conta(1, 'Yuri')
print(c.__dict__)

c.deposito(100)
print(c.__dict__)

c.deposito(50)
print(c.__dict__)