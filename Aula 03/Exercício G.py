"""Crie um array que o conteúdo seja nomes das cores. Em seguida remova apenas a cor "vermelho”, se houver."""


def delataCorVermelha():
    cores = []
    continuar = " "
    while continuar != "nao":
        cor = str(input("Me fale uma cor: "))
        cores.append(cor)
        continuar = str(input("Deseja continuar? [sim / nao ]").lower())
    if "vermelho" in cores:
        cores.remove("vermelho")
        print("A cor vermelha foi removida")
    print(cores)


delataCorVermelha()
