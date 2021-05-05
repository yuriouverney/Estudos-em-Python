"""
Faça um programa que imprima na tela os números de 1 a 20,
um abaixo do outro. Depois modifique o programa para que
ele mostre os números um ao lado do outro.
"""
def iniciar():
    for i in range(21):
        print(i)
    print(list(range(1, 21)))
if(__name__ == "__main__"):
    iniciar()
