"""Faça um programa que leia 5 números e informe o maior número."""

def iniciar():
    while True:
        try:
            numero_um = int(input("Digite o primeiro número: "))
            numero_dois = int(input("Digite o segundo número: "))
            numero_tres = int(input("Digite o terceiro número: "))
            numero_quatro = int(input("Digite o quarto número: "))
            numero_cinco = int(input("Digite o quinto número: "))

            if numero_um > numero_dois and numero_um > numero_tres and numero_um > numero_quatro and numero_um > numero_cinco:
                print(f"O primeiro número digitado ({numero_um}) é o maior")
            elif numero_dois > numero_um and numero_dois > numero_tres and numero_dois > numero_quatro and numero_dois > numero_cinco:
                print(f"O segundo número digitado ({numero_dois}) é o maior")
            elif numero_tres > numero_um and numero_tres > numero_dois and numero_tres > numero_quatro and numero_tres > numero_cinco:
                print(f"O terceiro número digitado ({numero_tres}) é o maior")
            elif numero_quatro > numero_um and numero_quatro > numero_dois and numero_quatro > numero_tres and numero_quatro > numero_cinco:
                print(f"O quarto número digitado ({numero_quatro}) é o maior")
            elif numero_cinco > numero_um and numero_cinco > numero_dois and numero_cinco > numero_tres and numero_cinco > numero_quatro:
                print(f"O quinto número digitado ({numero_cinco}) é o maior")

        except ValueError:
            print("Você deve digitar apenas números")
            continue

if(__name__ == "__main__"):
    iniciar()