def main():
    matriz = []
    valores = []

    lista = []
    matrizT = []

    matrizTransposta = []
    tamlinha = int(input("Qual o tamanho da linha matriz? min 1 | max 10 "))
    tamColuna = int(input("Qual o tamanho da coluna matriz? min 1 | max 10 "))
    while 0 >= tamlinha > 10 and 0 >= tamColuna > 10:
        tamlinha = int(input("Qual o tamanho da linha matriz? min 1 | max 10 "))
        tamColuna = int(input("Qual o tamanho da coluna matriz? min 1 | max 10 "))
    for i in range(tamColuna):
        for v in range(tamlinha):
            valor = int(input(f"Digite um valor para a matriz no indice {i}: "))
            valores.append(valor)
        matriz.append(valores[:])
        valores.clear()
    print(matriz)

    cont = 0
    ajudante1 = 0
    ajudante2 = 0
    while cont < len(matriz) + 1:
        for i in range(ajudante1, len(matriz)):
            for j in range(ajudante2):
                matrizT.append(matriz[i][j])
        matrizTransposta.append(matrizT)
        cont += 1
        ajudante1 += 1
        ajudante2 += 1
    print(matrizTransposta)


main()
