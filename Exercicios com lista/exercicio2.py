""""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."""

def iniciar():
    try:
        lista = []
        i = 0
        print("Você deve digitar 10 números")
        for i in range(10):
            lista.append(int(input(f'Digite o número {i+1}:\n')))
        lista.reverse()
        print(lista.reverse)
    except ValueError:
        print("Você deve digitar apenas números")
        return iniciar()

if(__name__ == "__main__"):
    iniciar()