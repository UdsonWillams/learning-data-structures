"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato."""


def main():
    valorMenor = 999999
    for i in range(1, 4):
        produto = int(input(f"Qual o valor do produto {i}? "))
        if produto < valorMenor:
            valorMenor = produto
            id = i
    print(f"O produto de menor valor foi {id} com valor de R${float(valorMenor):.2f}")


main()
