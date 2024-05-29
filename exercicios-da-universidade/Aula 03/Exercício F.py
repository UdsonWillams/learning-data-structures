"""Crie um programa no qual o usuário digitará 5 nomes num vetor
(OBRIGATÓRIO TER SEU NOME INCLUÍDO NO VETOR). Em seguida:

a) Mostre os valores na tela.
b) Adicione seu sobrenome na posição do seu nome no array.
c) Imprima o resultado na tela."""
from random import randint


def nomeSobrenome():
    nomes = []
    for i in range(0, 5):
        nome = str(input(f"Digite o {i + 1}° nome: "))
        nomes.append(nome)
    nomeProprio = str(input("Qual o seu nome? "))
    nomes.insert(randint(0, len(nomes)), nomeProprio)
    sobrenome = str(input("Qual o seu sobrenome ? "))
    for i in nomes:
        if i == nomeProprio:
            lugar = nomes.index(i)
            nomes.insert(lugar + 1, sobrenome)
    print(nomes)


nomeSobrenome()
