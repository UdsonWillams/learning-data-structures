"""Crie um programa que o usuário digite uma sequência de valores (de tamanho dinâmico)
numa única variável, chamada registro. Em seguida, mostre os valores armazenados."""


def main():
    registro = []
    cont = 0
    continuar = "S"
    while continuar == "S":
        valores = input("DIGITE OQUE QUISER ")
        registro.append(valores)
        continuar = str(input("Deseja continuar? [S / N]").upper()[0])
    for r in registro:
        print(f"Na posição {cont} está o valor {r}")
        cont += 1


main()
