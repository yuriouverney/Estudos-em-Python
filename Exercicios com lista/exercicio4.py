""""Faça um Programa que leia um vetor de 10 caracteres, e
diga quantas consoantes foram lidas. Imprima as consoantes."""

def iniciar():
    try:
        lista = []
        i = 0
        consoantes = 0
        print("Você deve digitar 10 caracteres")
        for i in range(10):
            lista.append(input(f'Digite um caracter {i+1}:\n'))
            char = lista[i]
            if (char not in ('a', 'e', 'i', 'o', 'u')):
                consoantes += 1
        print(consoantes)
    except ValueError:
        print("Você deve digitar apenas números")
        return iniciar()

if(__name__ == "__main__"):
    iniciar()