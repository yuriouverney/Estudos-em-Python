'''Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
Atributos: Nome, Fome, Saúde e Idade
b. Métodos: Alterar Nome, Fome, Saúde e Idade;
 Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração,
  o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja,
  um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela
  pode ser calculada a qualquer momento.'''

class Tamaguchi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        if fome in range(0,101):
            self.fome = fome
        else:
            print("digite uma fome entre 0-100")
        if saude in range(0,101):
            self.saude = saude
        else:
            print("digite uma saúde entre 0-100")

        self.idade = idade
        Tamaguchi.humor(0, fome, saude)

    def alterarNome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def alterarFome(self, novo_fome):
        if novo_fome in range(0,101):
            self.fome = novo_fome
        else:
            print("digite uma fome entre 0-100")
        Tamaguchi.humor(0, novo_fome, self.saude)
        return self.fome

    def alterarSaude(self, novo_saude):
        if novo_saude in range(0,101):
            self.saude = novo_saude
        else:
            print("digite uma saúde entre 0-100")
        Tamaguchi.humor(0, self.fome, novo_saude)
        return self.saude

    def alterarIdade(self, novo_idade):
        self.idade = novo_idade
        return self.idade

    def humor(self, fome, saude):
        if fome in range(90,101) and saude in range(90,101):
            print("Tamaguchi Muito Feliz")
        elif fome in range(70, 90) and saude in range(70, 90):
            print("Tamaguchi Feliz")
        elif fome in range(40,70) and saude in range(40,70):
            print("Tamaguchi Triste")
        else:
            print("Tamaguchi Muito Triste")


ti = Tamaguchi('Yuri', 100, 100, 2)
print(ti.__dict__)
ti.alterarFome(90)
print(ti.__dict__)
ti.alterarSaude(10)
print(ti.__dict__)