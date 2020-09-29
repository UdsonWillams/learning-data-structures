def pedirNumero():
    num = int(input("DIGITE UM NUMERO PARA VERIFICAÇÃO: "))
    return num


def main(num):
    numPali1 = str(num)
    numPali2 = str(num)
    cont1 = 0
    cont2 = -1
    total = int(len(numPali1))
    while cont1 < len(numPali1):
        if numPali1[cont1] == numPali2[cont2]:
            print(numPali1[cont1], end=" ")
            cont1 += 1
            cont2 -= 1
            if cont1 == total:
                print("\nESTE NUMERO É UM PALINDROMO")
        else:
            print("\nESTE NUMERO NÃO É UM PALINDROMO")
            cont1 = total + 1


num = pedirNumero()
main(num)

