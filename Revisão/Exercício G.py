def um(num1, num2):
    mostre = num1 * 2 + (num2 / 2)
    return int(mostre)


def dois(num1, num3):
    mostre = num1 * 3 + num3
    return int(mostre)


def treis(num3):
    mostre = num3**3
    return mostre


def main():
    num1 = int(input("Digite 1 numero "))
    num2 = int(input("Digite outro numero "))
    num3 = float(input("Digite 1 numero real "))

    resultado1 = um(num1, num2)
    print(resultado1)
    resultado2 = dois(num1, num3)
    print(resultado2)
    resultado3 = treis(num3)
    print(resultado3)


main()
