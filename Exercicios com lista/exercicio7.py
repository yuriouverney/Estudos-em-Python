""""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."""
import numpy as np

def iniciar():
    try:
        lista = []
        i = 0
        soma = 0
        multiplicacao = 0

        print("Você deve digitar 5 números")
        for i in range(5):
            lista.append(int(input(f'Digite o número {i+1}:\n')))
        print(f"Os números digitados foram: {lista}")
        soma = sum(lista)
        print(f"a soma de todas as notas é igual a: {soma}")
        multiplicacao = np.prod(lista)
        print(f"a multiplicação de todas as notas é igual a: {multiplicacao}")

    except ValueError:
        print("Você deve digitar apenas números")
        return iniciar()
if(__name__ == "__main__"):
    iniciar()