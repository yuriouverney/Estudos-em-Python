# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

def iniciar():
    while True:
        try:
            nome = input("digite seu Nome: ")
            contador_letras_nome = len(nome)
            if (contador_letras_nome <= 3):
                print ("seu nome deve conter mais de 3 caractéres")
                continue
            else:
                pass

            idade = int(input("digite sua idade: "))

            if (idade > 0 and idade < 150):
                pass
            else:
                print ("sua idade deve ser entre 0 e 150 anos.")
                continue

            salario = float(input("Digite seu salário: "))

            if (salario >= 0):
                pass
            else:
                print("o salário deve ser maior ou igual a 0")
                continue

            sexo = input("Digite (F) se for do sexo feminino e (M) se for do masculino: ")

            if(sexo == "f" or sexo == "m"):
                pass
            else:
                print("você deve digitar F para feminino ou M para masculino")
                continue

            estado_civil = input("Digite (S) se for solteiro, (C) se for casado"
                                 ", (V) se for viúvo e (d) se for divorciado: ")

            if (estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d"):
                pass
            else:
                print("Você deve digitar (S) se for solteiro, (C) se for casado"
                                 ", (V) se for viúvo e (D) se for divorciado:")
                continue

            if (sexo == "m"):
                sexo = "masculino"
            elif (sexo == "f"):
                sexo = "feminino"

            if (estado_civil == "s"):
                estado_civil = "solteiro"
            elif (estado_civil == "c"):
                estado_civil = "casado"
            elif (estado_civil == "v"):
                estado_civil = "viuvo"
            elif (estado_civil == "d"):
                estado_civil = "divorciado"

            print(f"Nome: {nome}, Idade: {idade}, Salário: {salario}, Sexo: {sexo}, Estado civil: {estado_civil}")

        except ValueError:
            continue

if(__name__ == "__main__"):
    iniciar()
