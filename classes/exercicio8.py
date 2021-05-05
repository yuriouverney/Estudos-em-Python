'''Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago)
 e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente,
 criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando
  o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro.
  É possível criar um macaco canibal?
'''

class Macaco:
    def __init__(self, nome, bucho = []):
        self.nome = nome
        self.bucho = bucho

    def comer(self, alimento):
        if len(self.bucho) < 3:
            self.bucho.append(alimento)
        else:
            print(f"{self.nome} está cheio!")

    def verBucho(self, ver):
        print(self.bucho)

    def digerir(self, numero):
        if numero > 3:
            numero = 3
        if numero <= 3:
            while numero > 0:
                self.bucho.pop()
                numero -= 1

t1 = Macaco('yuri', )
t1.comer('banana')
t1.comer('arroz')
t1.comer('feijão')
t1.verBucho('')
t1.digerir(2)
t1.verBucho('')