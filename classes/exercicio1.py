class Bola:
    def __init__(self, circunferencia=10, cor='azul', material='couro', loop='s'):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        self.loop = loop

    def trocaCor():
        Bola.cor = input("digite a cor: ")
        Bola.mostraCor()

    def mostraCor():
        print(f'A cor da bola é {Bola.cor}')
        Bola.loop = input("Deseja alterar a cor da bola? (s/n): ")
        Bola.loop = Bola.loop.upper()
        if Bola.loop == 'S':
            Bola.trocaCor()
        else:
            print("Programa Finalizado")
            exit()

Bola.trocaCor()