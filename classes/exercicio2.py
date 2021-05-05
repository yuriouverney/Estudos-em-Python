class Quadrado:
    def __init__(self, tamanholado, area):
        self.tamanholado = tamanholado
        self.area = area

    def mudarValorLado():
        Quadrado.tamanholado = int(input("Digite o valor do lado do quadrado: "))
        Quadrado.retornarValorLado()

    def retornarValorLado():
        print(f"o valor do lado do quadrado é {Quadrado.tamanholado}")
        Quadrado.calcularArea()

    def calcularArea():
        Quadrado.area = Quadrado.tamanholado * Quadrado.tamanholado
        print(f'A área total do quadrado é {Quadrado.area}')
        continuar = input('Deseja continuar? (s/n): ')
        continuar = continuar.upper()
        if continuar == 's':
            Quadrado.mudarValorLado()
        else:
            print('Programa finalizado!')
            exit()

Quadrado.mudarValorLado()