""""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares
no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores."""

def iniciar():
    try:
        numero = []
        par = []
        impar = []

        for i in range(20):

            digito = int(input("Digite um número: "))

            numero.append(digito)

            if (digito % 2) == 0:
                par.append(digito)
            else:
                impar.append(digito)

        print(numero)
        print(par)
        print(impar)

    except ValueError:
        print("Você deve digitar apenas números")
        return iniciar()
if(__name__ == "__main__"):
    iniciar()