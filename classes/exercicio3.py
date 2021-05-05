'''Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o
local.'''

class Retangulo:
    def __init__(self, base, altura, area, perimetro):
        self.base = base
        self.altura = altura
        self.area = area
        self.perimetro = perimetro

    def mudarValor():
        Retangulo.base = int(input("Digite o valor da base do retângulo: \n"))
        Retangulo.altura = int(input("Digite o valor da altura do retângulo: \n"))
        Retangulo.calcularArea()

    def calcularArea():
        Retangulo.area = Retangulo.base * Retangulo.altura
        Retangulo.calcularPerimetro()

    def calcularPerimetro():
        Retangulo.perimetro = (2*Retangulo.base)+(2*Retangulo.altura)
        Retangulo.retornarValores()

    def retornarValores():
        print(f'Um retângulo de base {Retangulo.base} e altura {Retangulo.altura}\n'
              f'corresponde à uma área de {Retangulo.area} e um perímetro de {Retangulo.perimetro}.')
        continuar = input('Você deseja fazer cálculos com valores diferentes? (s/n): \n')
        continuar = continuar.upper()
        if continuar == 'S':
            Retangulo.mudarValor()
        else:
            print('Programa finalizado!')
            exit()

Retangulo.mudarValor()