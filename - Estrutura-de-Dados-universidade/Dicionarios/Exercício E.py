def main():
    dicionario = {}
    lista1 = []
    lista2 = []

    for i in range(3):
        dicionario["nome"] = str(input(f"Nome: "))
        dicionario["endereco"] = str(input("Endereço: "))
        dicionario["cpf"] = int(input("Qual o cpf?: "))

        lista1.append(dicionario.copy())
        lista2.append(lista1[:])
        lista1.clear()
    del lista1

    i = 0
    for d in lista2:
        print(f"O {i + 1}° nome é: {d[0]['nome']}")
        print(f"O {i + 1}° endereço é: {d[0]['endereco']}")
        print(f"O {i + 1}° cpf é: {d[0]['cpf']}")
        print(30 * "-")
        i += 1


main()
