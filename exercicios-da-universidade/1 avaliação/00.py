def numVelasAniverasario(velasAlturaAniver: int):
    maiorAltura = max(velasAlturaAniver)
    maior = velasAlturaAniver.count(maiorAltura)
    print(f"Número de velas com a altura maxima é de: {maior}")


def main():
    velasAlturamain = []
    tamanhoVelasAltura = int(input("Qual o tamanho das velas?"))
    while tamanhoVelasAltura <= 1 or tamanhoVelasAltura >= 10**5:
        tamanhoVelasAltura = int(
            input(
                "VALOR INVALIDO\nPOR FAVOR DIGITE UM NOVO VALOR\nQual o tamanho "
                "das velas?"
            )
        )
    altura = input("Qual a altura das velas?")
    for v in altura.split(" "):
        if v.isnumeric():
            if 1 < int(v) < 10**7:
                velasAlturamain.append(int(v))
    while len(velasAlturamain) > tamanhoVelasAltura:
        velasAlturamain.pop()
    return velasAlturamain


velasAltura = main()
numVelasAniverasario(velasAltura)
