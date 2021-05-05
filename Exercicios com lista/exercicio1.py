""""Faça um Programa que leia um vetor de 5 números inteiros e mostre-os."""

def iniciar():
    try:
        lista = []
        i = 0
        print("Você deve digitar 5 números")
        for i in range(5):
            lista.append(int(input(f'Digite o número {i+1}:\n')))
        print(lista)
    except ValueError:
        print("Você deve digitar apenas números")
        return iniciar()
if(__name__ == "__main__"):
    iniciar()