# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

def iniciar():
    while True:
        try:
            numero_escolhido = int(input("Digite um número entre 1 e 10"))
            if (numero_escolhido > 0 and numero_escolhido <= 10):
                print(f"seu número escolhido foi {numero_escolhido}")
                break
            else:
                continue
        except ValueError:
            continue

if(__name__ == "__main__"):
    iniciar()
