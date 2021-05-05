"""
Altere o programa anterior permitindo ao usuário informar as
populações e as taxas de crescimento iniciais. Valide a
entrada e permita repetir a operação.
"""

def iniciar():
    try:
        pais1 = int(input("Adicione o valor da população do primeiro país "))
        pais1_taxa_crescimento = float(input("Adicione a taxa de crescimento em anos do primeiro país "))
        pais2 = int(input("Adicione o valor da população do segundo país "))
        pais2_taxa_crescimento = float(input("Adicione a taxa de crescimento em anos do segundo país "))
        anos = 0

    except ValueError:
        print("você deve digitar apenas números")
        return iniciar()

    if pais1 > pais2:
        inverte_valor_pop = pais1
        pais1 = pais2
        pais2 = inverte_valor_pop
        inverte_valor_taxa = pais1_taxa_crescimento
        pais1_taxa_crescimento = pais2_taxa_crescimento
        pais2_taxa_crescimento = pais1_taxa_crescimento
    elif pais1 == pais2:
        print("Os países já tem a mesma população!")

    while pais1 < pais2:
            pais1 = pais1 * ((pais1_taxa_crescimento/100) +1)
            pais2 = pais2 * ((pais2_taxa_crescimento/100) +1)

            anos += 1
            if pais1 >= pais2:
                print(f"demoraria {anos} anos para uma população passar a outra")

if(__name__ == "__main__"):
    iniciar()
