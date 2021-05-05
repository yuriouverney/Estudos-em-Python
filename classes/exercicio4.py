'''Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa
pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.'''

class Pessoa:
    idadecrescer = 21
    def __init__(self, nome, idade, peso, altura, acrescentaridade):
        self.nome = nome
        self.idade = idade
        self.peso = float(peso)
        self.altura = float(altura)
        self.envelhecer = envelhecer

    def atribuirValores():
        Pessoa.nome = input("Digite o nome da pessoa: \n")
        Pessoa.idade = float(input("Digite a idade da pessoa: \n"))
        Pessoa.peso = float(input("Digite o peso da pessoa: \n"))
        Pessoa.altura = float(input("Digite a altura da pessoa: \n"))
        Pessoa.envelhecer()

    def envelhecer():
        envelhecer = input("Você deseja adicionar idade a essa pessoa? (s/n): \n")
        envelhecer = envelhecer.upper()
        if envelhecer == 'S':
            Pessoa.acrescentaridade = float(input("Quantos anos você deseja adicionar? \n"))
        Pessoa.crescer()

    def crescer():
        acrescentarTamanho = 0
        while Pessoa.idade < 21.0 and Pessoa.acrescentaridade >= 1.0:
            Pessoa.idade += 1
            Pessoa.acrescentaridade -= 1
            acrescentarTamanho += 1
        Pessoa.idade = Pessoa.idade + Pessoa.acrescentaridade
        Pessoa.altura = Pessoa.altura + (acrescentarTamanho*0.5)
        Pessoa.engordar()

    def engordar():
        engordou = input("A pessoa engordou? (s/n) \n")
        engordou = engordou.upper()
        if engordou == 'S':
            valorengordou = float(input("Quantos quilos a pessoa engordou? \n"))
            Pessoa.peso += valorengordou
            Pessoa.resultados()
        else:
            Pessoa.emagrecer()

    def emagrecer():
        emagreceu = input("A pessoa emagreceu? (s/n) \n")
        emagreceu = emagreceu.upper()
        if emagreceu == 'S':
            valoremagrecer = float(input("Quantos quilos a pessoa emagreceu? \n"))
            Pessoa.peso -= valoremagrecer
        Pessoa.resultados()

    def resultados():
        print(f"Nome: {Pessoa.nome}, Idade: {int(Pessoa.idade)},"
              f"Peso {Pessoa.peso}, Altura: {Pessoa.altura} ")
        novaPessoa = input("Voce deseja fazer o processo com ouatra pessoa? (s/n): \n")
        novaPessoa = novaPessoa.upper()
        if novaPessoa == 'S':
            Pessoa.atribuirValores()
        else:
            print("Programa finalizado!")
            exit()

Pessoa.atribuirValores()


