"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
 inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada."""
from time import sleep
# Selecionando valores validos
num1 = int(input("DIGITE UM VALOR PARA A TABUADA: [ENTRE 1 E 10] "))
while num1 <= 0 or num1 > 10:
    print("VALOR INVALIDO, DIGITE UM VALOR ENTRE 1 E 10")
    num1 = int(input("DIGITE UM VALOR PARA A TABUADA: "))
#Com For
print(f"A TABUADA DE {num1} É:")
print("FAZENDO COM FOR")
for i in range(1, 11):
    sleep(0.5)
    print(f"{num1} x {i} = {num1 * i}")
print(30 * "=")
#Com While
cont = 1
print("FAZENDO COM WHILE")
while cont < 11:
    sleep(0.5)
    print(f"{num1} x {i} = {num1 * cont}")
    cont += 1
print(30 * "=")
