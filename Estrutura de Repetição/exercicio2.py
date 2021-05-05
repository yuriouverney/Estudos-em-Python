#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
# ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

def iniciar():
    while True:
        try:
            usuario = input("digite seu nome de usuário: ")
            senha = input("digite sua senha: ")

            if (usuario == senha):
                print(f"seu usuário e senha não podem ser iguais")
                continue
            else:
                print(f"Olá, {usuario}. Seja bem vindo!")
                break
        except ValueError:
            continue

if(__name__ == "__main__"):
    iniciar()
