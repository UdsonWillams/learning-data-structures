"""Crie um array que o conteúdo seja nomes das cores. Em seguida remova apenas a cor "vermelho”, se houver."""


def delataCorVermelha():
    cores = []
    continuar = " "
    while continuar != "nao":
        cor = str(input("Me fale uma cor: "))
        cores.append(cor)
        continuar = str(input("Deseja continuar? [sim / nao ]").lower())
    for i in range(0, len(cores)):
        if "vermelho" in cores:
            cores.remove("vermelho")
            print("A cor vermelha foi removida")
        else:
            print("Voce nao digitou vermelho")
    print(cores)


delataCorVermelha()
