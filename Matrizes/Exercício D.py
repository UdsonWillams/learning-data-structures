def main():
    matriz = [
        [1, 2, 3, 4], [5, 6, 7, 8]
    ]

    print(f"O valores são : {matriz}")

    for i in range(0, len(matriz)):
        ultimoValor = int(input("Digite um ultimo valor para a matriz "))
        matriz[i].append(ultimoValor)

    print(f"Os novos valores são {matriz}")


main()
