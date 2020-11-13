"""peça ao usuario para digitar uma matrix 4x4 E em seguida
conte e escreva os valores maiores que 10 que ela possui."""


def main():
    """
    preenchendo uma matriz de 4 linhas por 4 colunas
    """
    matriz = []
    valores = []
    for i in range(4):
        for v in range(4):
            valor = int(input(f"Digite um valor para a matriz no indice {i}: "))
            valores.append(valor)
        matriz.append(valores[:])
        valores.clear()
    print(matriz)

    """
    Descobrindo quantos valores maiores que 10 existem na matriz
    """
    contador = 0
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            if matriz[i][j] > 10:
                contador += 1

    print(f"Ao todo {contador} são maiores que 10")


main()
