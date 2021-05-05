'''Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário
 deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
 Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.'''

class Tv:
    def __init__(self, canal, volume):
        if canal in range(1,501):
            self.canal = canal
        else:
            self.canal = 1
            print("Canal inválido. 1-500")
        if volume in range(0, 101):
            self.volume = volume
        else:
            self.volume = 0
            print("Volume inválido. 0-100")

    def mudar_canal(self, novo_canal):
        if novo_canal in range(1,501):
            self.canal = novo_canal
        else:
            print("Canal inválido. 1-500")
        return self.canal

    def mudar_volume(self, novo_volume):
        if novo_volume in range(0,101):
            self.volume = novo_volume
        else:
            print("Volume inválido. 0-100")
        return self.volume

mudar = Tv(15,100)
print(mudar.__dict__)
mudar.mudar_volume(100)
print(mudar.__dict__)
mudar.mudar_canal(100)
print(mudar.__dict__)