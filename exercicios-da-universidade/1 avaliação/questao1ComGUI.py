import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
            [sg.Text("LOGIN")], [sg.InputText()],
            [sg.Text("SENHA")], [sg.InputText()],
            [sg.Button("FAZER LOGIN")],
            [sg.Text("SE INSCREVER")]]
            
tela = sg.Window("LOGIN", layout)

while True:
    evento, valores = tela.read()

    if evento == sg.WIN_CLOSED or evento == "CANCELAR":  # if user closes window or clicks cancel
        break


tela.close()
