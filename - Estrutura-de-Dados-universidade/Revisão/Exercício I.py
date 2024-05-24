"""Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo. """


def main():
    valor = int(input("Digite um numero: "))
    if valor % 2 == 0:
        print(f"O valor digitado foi: {valor} | Este valor é PAR")
    else:
        print(f"O valor digitado foi: {valor} | Este valor é IMPAR")


main()
