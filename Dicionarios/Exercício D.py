def main():
    dicionario = {}
    lista = []

    for i in range(5):
        codigoBarra = str(input(f"Codigo de barra do {i + 1}° Produto? "))
        produto = str(input("Qual o nome do produto? "))
        preco = str(input("Qual o preço desse produto: "))

        lista.append(produto)
        lista.append(preco)
        dicionario[codigoBarra] = lista[:]
        lista.clear()

    for i in range(2):
        removerCodigo = str(input("Remova dois produtos pelo codigo de barra: [DIGITE O CODIGO]"))
        for k in dicionario.keys():
            if k == removerCodigo:
                remover = k
        dicionario.pop(remover)

    print(dicionario)

    for i in range(2):
        print("Remova os produtos pelo nome do produto e pelo preço:")
        removerNome = str(input("NOME: "))
        removerPreco = str(input("PRECO DO PRODUTO: "))

        for v in dicionario.values():
            if v[0] == removerNome and v[1] == removerPreco:
                v[0] = None
                v[1] = None

    print(dicionario)


main()
