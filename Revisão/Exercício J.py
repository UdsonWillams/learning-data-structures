"""Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Gênero Inválido. """


def main(genero):
    if genero == "F":
        print("F - Feminino")
    elif genero == "M":
        print("M - Masculino")
    elif genero != "F" and genero != "M":
        print("Gênero Invalido")


genero = str(input("Qual o seu gênero? [F / M]").upper()[0])
main(genero)
