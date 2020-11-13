def main():
    matriz = [
        [39, 14, 27],
        [21, 83, 92],
        [31, 12, 43]
    ]

    print(f"O valores são : {matriz}")

    for i in range(0, len(matriz)):
        matriz[i].pop()

    print(f"Os novos valores são {matriz}")


main()
