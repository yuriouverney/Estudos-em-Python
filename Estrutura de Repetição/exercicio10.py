# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

def iniciar():
    try:
        numero_um = int(input("Digite o primeiro número"))
        numero_dois = int(input("Digite o segundo número"))
        diferenca = 0

        if numero_um > numero_dois:
            verifica = numero_um - numero_dois
        else:
            verifica = numero_dois - numero_um
        while verifica > diferenca:
            diferenca += 1
            print(diferenca)

    except ValueError:
        print("digite apenas números inteiros: ")
        return iniciar()

if(__name__ == "__main__"):
    iniciar()
