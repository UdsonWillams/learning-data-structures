def main():

    dicionario = {}
    lista = []

    for i in range(3):
        cep = str(input(f"Qual o cep do {i+  1}° usuario? "))
        enderecoUsuario = str(input("Qual o endereço do usuario: "))
        lista.append(enderecoUsuario)
        dicionario[cep] = lista[:]
        lista.clear()

    print("Deseja buscados por qual metodo? [1 - POR CEP | 2 - POR ENDEREÇO ]")

    metodo = int(input("Diga o metodo de busca: "))
    while metodo > 0 and metodo > 2:
        metodo = int(input("VALOR INVALIDO\nDiga o metodo de busca: "))

    if metodo == 1:
        pesquisaCep = str(input("Qual o numero do cep para verificação? "))
        for i in dicionario.keys():
            if i == pesquisaCep:
                print(f"O endereço é: {dicionario[i]}")

    elif metodo == 2:
        pesquisaEndereco = str(input("Qual o endereço de pesquisa? "))
        for k in dicionario.keys():
            if dicionario[k][0] == pesquisaEndereco:
                print(f"O CEP é: {k}")


main()
