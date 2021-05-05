import matplotlib.pyplot as plt

def grafico():
    import matplotlib.pyplot as plt

    notas_matematica = ['Matemática',8,7,6,6,7,7,8,10]
    notas_portugues = ['Português',9,9,9,8,5,6,8,5]
    notas_geografia = ['Geografia',10,10,6,7,7,7,8,7]

    notas = [notas_matematica, notas_portugues, notas_geografia]

    for nota in notas:
        x = list(range(1, 9))
        y = nota[1:]
        plt.plot(x, y, marker='o')
        plt.xlabel('Provas')
        plt.ylabel('Notas')
        plt.title(nota[0])
        plt.grid()
        plt.show()

if(__name__ == "__main__"):
    grafico()