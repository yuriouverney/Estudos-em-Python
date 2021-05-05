""""Faça um Programa que peça as quatro notas de 10 alunos,
calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0."""

def iniciar():
    try:
        nota = []
        acima_media = []
        abaixo_media = []

        for i in range(10):

            digito = int(input(f"Digite um número de 0 a 10 - Digite a {i+1} nota: \n "))
            nota.append(digito)
            if digito >= 0 and digito <= 10:
                pass
            else:
                print("Você deve adicionar uma nota de 0 a 10!")
                return iniciar()
            if digito >= 7:
                acima_media.append(digito)
            else:
                abaixo_media.append(digito)

        print(nota)
        print(acima_media)
        print(abaixo_media)

    except ValueError:
        print("Você deve digitar apenas números")
        return iniciar()
if(__name__ == "__main__"):
    iniciar()