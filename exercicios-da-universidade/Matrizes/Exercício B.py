def main():
    matriz = [[39, 14, 27], [21, 83, 92], [31, 12, 43]]

    for i in range(0, len(matriz)):
        for v in range(0, len(matriz)):
            print(f"O valor de: {matriz[i][v]} * 7 é de: {matriz[i][v] * 7}")


main()
