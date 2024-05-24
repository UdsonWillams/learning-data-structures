def palindromo(num):
    palindromo = str(num)
    cont1 = 0
    cont2 = -1
    while cont1 < len(palindromo):
        if palindromo[cont1] == palindromo[cont2]:
            print(palindromo[cont1], end=" ")
            cont1 += 1
            cont2 -= 1
            if cont1 == len(palindromo):
                print("\nESTE NUMERO É UM PALINDROMO")
        else:
            print("\nESTE NUMERO NÃO É UM PALINDROMO")
            cont1 = len(palindromo) + 1


def main():
    numero = int(input("DIGITE UM NUMERO PARA VERIFICAÇÃO: "))
    return numero


while True:
    num = main()
    palindromo(num)
    continuar = str(input("DESEJA CONTINUAR? [S / N]").upper()[0])
    if continuar == "N":
        break
