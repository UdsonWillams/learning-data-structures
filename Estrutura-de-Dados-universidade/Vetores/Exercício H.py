"""Crie um array referente aos anos de nascimento das 5 pessoas mais próximas a você. Em seguida:
- Ordene o array  na ordem crescente e mostre o resultado;
- Ordene o array na ordem decrescente e mostre o resultado;"""


def main():
    dataNascimento = []
    for i in range(5):
        data = int(input("Qual o ano que você nasceu? "))
        dataNascimento.append(data)

    dataNascimento.sort()
    print("Os anos em ordes crescente são: ", dataNascimento)
    print(30 * "-")
    dataNascimento.sort(reverse=True)
    print("Os anos em ordes decrescente são: ", dataNascimento)


main()
