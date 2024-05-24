import PySimpleGUI as sg


def palindromo(num):
    palindromo = str(num)
    cont1 = 0
    cont2 = -1
    while cont1 < len(palindromo):
        if palindromo[cont1] == palindromo[cont2]:
            cont1 += 1
            cont2 -= 1
            if cont1 == len(palindromo):
                palindromoVerdade = True
        else:
            cont1 = len(palindromo) + 1
            palindromoVerdade = False
    return palindromoVerdade


def main():
    sg.theme('DarkAmber')
    # layout do interface
    layout = [[sg.Text("SEU NUMERO É UM PALINDROMO?")],
              [sg.Text("DIGITE UM NUMERO PARA VERIFICAÇÃO"), sg.InputText(size=(10, 10))],
              [sg.Button('Ok'), sg.Button('Fechar')]]
    tela = sg.Window('VERIFICADOR DE PALINDROMO', layout)
    # Loop para processar os eventos e pegar o valor dos inputs
    while True:
        evento, valor = tela.read()
        if evento == sg.WIN_CLOSED or evento == 'Fechar':  # Caso o usuario feche a janela ou click em cancelar
            break
        if palindromo(valor[0]) is True:
            sg.Popup("O VALOR É UM PALINDROMO")
        else:
            sg.Popup("O VALOR NÃO É UM PALINDROMO")


main()

