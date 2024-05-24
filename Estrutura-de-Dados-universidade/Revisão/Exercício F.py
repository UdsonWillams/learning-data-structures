"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tintaé
vendida em latas de 18 litros, que custamR$ 80,00. Informe ao usuário a quantidades de latas de tinta a
serem compradas e o preço total. """

areaASerPintada = int(input("Qual o tamanho da area a ser pintada? "))
indice = 54
i = 2
if areaASerPintada <= 54:
    latas = 1
    valor = 80
else:
    while indice < areaASerPintada:
        if areaASerPintada > 54:
            indice = 54 * i
            if indice < areaASerPintada:
                i += 1
            if indice >= areaASerPintada:
                latas = i
                valor = 80 * i
print(f"São necessarias {latas} lata(s) de tinta\nE ao todo iram custar R${valor:.2f}")
