def main():
    inicio = int(input("n° de inicio da sequencia "))
    fim = int(input("n° de fim da sequencia "))
    cont = inicio
    print("com for")
    for i in range(inicio, fim + 1):
        print(i**2, end=" ")
    print("\ncom while")
    while cont < fim + 1:
        print(cont**2, end=" ")
        cont += 1


main()
