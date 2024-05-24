from time import sleep

fatorial = int(input("Digite um numero: "))
fatorialIncio = fatorial
incre = 0
result = 1
# Selecionando valores validos
while fatorial <= 0:
    print("VALOR INVALIDO, POR FAVOR DIGITE UM VALOR VALIDO")
    fatorial = int(input("Digite um numero válido: "))
print(30 * "=")
print("COM FOR")
# com for
for incre in range(1, fatorial):
    result *= fatorial
    fatorial -= 1
print(f"O fatorial de {fatorialIncio} é: {result}")
print(30 * "=")
# com while
sleep(1)
incre = 1
result = 1
print("COM WHILE")
while incre <= fatorialIncio:
    result *= incre
    incre += 1
print(f"O fatorial de {fatorialIncio} é igual a: {result}")
print(30 * "=")
