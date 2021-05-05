"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela
deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente"."""

def iniciar():
    try:
        lista = []
        i = 0
        count = 0
        print("Você deve responder o questionário com (1) para sim ou (0) para não")

        lista.append(int(input(f'Telefonou para a vítima? digite (1) para sim ou (0) para não:\n')))
        lista.append(int(input(f'Esteve no local do crime? digite (1) para sim ou (0) para não:\n')))
        lista.append(int(input(f'Mora perto da vítima? digite (1) para sim ou (0) para não:\n')))
        lista.append(int(input(f'Devia para a vítima? digite (1) para sim ou (0) para não:\n')))
        lista.append(int(input(f'Já trabalhou com a vítima? digite (1) para sim ou (0) para não:\n')))

        soma_respostas = 0
        for i in lista:  # soma o número de respostas
            soma_respostas += int(i)
        if (soma_respostas < 2):
            print("\nInocente")
        elif (soma_respostas == 2):
            print("\nSuspeita")
        elif (3 <= soma_respostas <= 4):
            print("\nCúmplice")
        elif (soma_respostas == 5):
            print("\nAssassino")

    except ValueError:
        print("Você deve digitar apenas números")
        return iniciar()
if(__name__ == "__main__"):
    iniciar()