"""
Elabore um programa que cria um array de nomes de países
e outro array com nomes de cidades. Cada uma das criações
devem ser feitas com métodos diferentes.
"""


def nomePaises():
    paises = []
    continuar = " "
    while continuar != "nao":
        nome = str(input("Digite o nome do pais: "))
        paises.append(nome)
        print("Valor adicionado a lista")
        continuar = str(input("Deseja continuar? "))
        print(paises)


def nomeCidades():
    cidades = []
    tamanho = int(input("Qual o tamanho da lista que você deseja? "))
    for i in range(0, tamanho):
        cidades.append(i)
    for i in range(0, len(cidades)):
        cidade = str(input("Digite o nome da cidade "))
        cidades.insert(i, cidade)
        cidades.pop()
    print(cidades)


nomeCidades()
nomePaises()
