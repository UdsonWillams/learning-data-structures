"""Crie um programa no qual o usuário digitará 5 nomes.
Todos os cinco nomes serão salvos no vetor chamado "registros”. Em seguida:

a) Mostre o que o usuário digitou na tela;
b) O programa pedirá outro nome, que será adicionado no fim do vetor "registros”;
c) O programa pedirá outro nome, que será adicionado na 2ª posição do vetor "registros”;
d) Imprima o resultado na tela."""


def registro():
    registros = []
    for i in range(0, 5):
        nome = str(input(f"Digite o {i + 1}° nome: "))
        registros.append(nome)
    outroNomeB = str(input("Digite um novo nome a ser adicionado: "))
    registros.append(outroNomeB)
    outroNomeC = str(input("Digite um novo nome a ser adicionado: "))
    registros.insert(1, outroNomeC)
    print(registros)


registro()
