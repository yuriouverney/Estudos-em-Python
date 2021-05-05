""""Faça um Programa que leia 4 notas, mostre as notas e a média na tela."""

def iniciar():
    try:
        notas = []
        i = 0
        media = 0
        print("Você deve digitar 4 notas")
        for i in range(4):
            notas.append(int(input(f'Digite o número {i+1}:\n')))
            media += notas[i]
        print(notas)
        media = media/(i+1)
        print(media)

    except ValueError:
        print("Você deve digitar apenas números")
        return iniciar()

if(__name__ == "__main__"):
    iniciar()