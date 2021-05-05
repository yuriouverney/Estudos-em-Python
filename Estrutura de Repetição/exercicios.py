import exercicio1
import exercicio2
import exercicio3
import exercicio4
import exercicio5
import exercicio6
import exercicio7
import exercicio8
import exercicio9
import exercicio10

def escolhe_exercício():
    print("*********************************")
    print("*****Estrutura de Repetição******")
    print("*******Escolha o exercicio!******")
    print("*********************************")

    print("Digite (1) para ir ao exercício 1")
    print("Digite (2) para ir ao exercício 2")
    print("Digite (3) para ir ao exercício 3")
    print("Digite (4) para ir ao exercício 4")
    print("Digite (5) para ir ao exercício 5")
    print("Digite (6) para ir ao exercício 6")
    print("Digite (7) para ir ao exercício 7")
    print("Digite (8) para ir ao exercício 8")
    print("Digite (9) para ir ao exercício 9")
    print("Digite (10) para ir ao exercício 10")

    exercicio = int(input("Qual exercício? "))

    if(exercicio == 1):
        print("Iniciado exercício 1")
        exercicio1.iniciar()
    elif(exercicio == 2):
        print("Iniciado exercício 2")
        exercicio2.iniciar()
    elif(exercicio == 3):
        print("Iniciado exercício 3")
        exercicio3.iniciar()
    elif(exercicio == 4):
        print("Iniciado exercício 4")
        exercicio4.iniciar()
    elif(exercicio == 5):
        print("Iniciado exercício 5")
        exercicio5.iniciar()
    elif (exercicio == 6):
        print("Iniciado exercício 6")
        exercicio6.iniciar()
    elif (exercicio == 7):
        print("Iniciado exercício 7")
        exercicio7.iniciar()
    elif (exercicio == 8):
        print("Iniciado exercício 8")
        exercicio8.iniciar()
    elif (exercicio == 9):
        print("Iniciado exercício 9")
        exercicio9.iniciar()
    elif (exercicio == 10):
        print("Iniciado exercício 10")
        exercicio10.iniciar()

if(__name__ == "__main__"):
    escolhe_exercício()
