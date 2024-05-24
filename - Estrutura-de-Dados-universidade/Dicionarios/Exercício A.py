def main():
    dicionario = {}
    lista = []

    for i in range(5):
        nomeUsuario = str(input("Qual o nome do usuario? "))
        nascimentoUsuario = str(input("Data de nascimento do usuario: "))
        enderecoUsuario = str(input("Endereço do usuario: "))
        lista.append(nascimentoUsuario)
        lista.append(enderecoUsuario)
        dicionario[nomeUsuario] = lista[:]
        lista.clear()
    print(dicionario)


main()
