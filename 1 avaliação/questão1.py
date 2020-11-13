def numVelasAniverasario(velasAlturaAniver):
    maiorAltura = max(velasAlturaAniver)
    maior = velasAlturaAniver.count(maiorAltura)
    print(f"Número de velas com a altura maxima é de: {maior}")


def main():
    velasAlturamain = []
    tamanhoVelasAltura = int(input("Qual o tamanho das velas?"))
    while tamanhoVelasAltura <= 1 or tamanhoVelasAltura >= 10**5:
        tamanhoVelasAltura = int(input("VALOR INVALIDO\nPOR FAVOR DIGITE UM NOVO VALOR\nQual o tamanho "
                                       "das velas?"))
    for i in range(0, tamanhoVelasAltura):
        altura = int(input("Qual a altura das velas?"))
        while altura < 1 or altura > 10**7:
            altura = int(input("VALOR INVALIDO\nPOR FAVOR DIGITE UM NOVO VALOR\nQual a altura das velas?"))
        velasAlturamain.append(altura)
    return velasAlturamain


velasAltura = main()
numVelasAniverasario(velasAltura)
