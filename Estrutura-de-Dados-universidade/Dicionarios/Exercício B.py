def main():

    dicionario = {}
    lista = []

    for i in range(2):
        cep = str(input(f"Qual o cep do {i+  1}° usuario? "))
        enderecoUsuario = str(input("Qual o endereço do usuario: "))
        lista.append(enderecoUsuario)
        dicionario[cep] = lista

    print("CEPs Cadastrados")
    for i in dicionario.keys():
        print(f"CEPs: {i}")


main()
