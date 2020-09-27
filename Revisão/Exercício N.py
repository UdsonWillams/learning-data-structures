clientesAntes = int(input("Quantos clientes foram atendidos? "))
"""if clientesAntes < 6:
    for i in range(0, clientesAntes):
        mediaTotal = 0
        tempo = int(input(f"Quantos minutos o cliente {i+1} Passou no banco?"))
        mediaTotal += tempo
    mediaFinal = mediaTotal / clientesAntes
    print(f"O tempo de espera no banco é em média de {mediaFinal:.2f}")
else:
    mediaFinal = 0
    print("Numero de clientes invalido")
"""
if clientesAntes >= 6:
    while clientesAntes >= 6:
        clientesAntes = int(input("Por favor, responda um numero valido entre 1 e 5\nQuantos clientes foram atendidos? "))
cont = 0
mediaTotal = 0
while cont < clientesAntes:
    tempo = int(input(f"Quantos minutos o cliente {cont + 1} Passou no banco?"))
    mediaTotal += tempo
    cont += 1
mediaFinal = mediaTotal / clientesAntes
print(f"O tempo de espera no banco é em média de {mediaFinal:.2f}")