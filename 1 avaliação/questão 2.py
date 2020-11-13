def diaDoProgramador(anoDiaProg):
    # calendario_juliano
    if 1700 <= anoDiaProg <= 1917:
        if anoDiaProg % 4 == 0:
            dataDiaProg = "12.09." + str(anoDiaProg)
        else:
            dataDiaProg = "13.09." + str(anoDiaProg)
    # calendario gregoriano
    if anoDiaProg > 1918:
        if anoDiaProg % 4 == 0 and anoDiaProg % 100 != 0 or anoDiaProg % 400 == 0:
            dataDiaProg = "12.09." + str(anoDiaProg)
        else:
            dataDiaProg = "13.09." + str(anoDiaProg)
    # entrando no calendario gregoriano
    elif anoDiaProg == 1918:
        dataDiaProg = "26.09.1918"

    print(f"Neste ano o dia do programador seria em {dataDiaProg}")
    return dataDiaProg


def main():
    # requisição do ano
    anoMain = int(input("Digite o ano: "))
    while anoMain < 1700 or anoMain > 2700:
        anoMain = int(input("Ano invalido, digite novamente: "))
    return anoMain


ano = main()
diaDoProgramador(ano)
