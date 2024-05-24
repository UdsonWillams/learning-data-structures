def main():
    matriz = []
    dados = []
    for i in range(3):
        nome = str(input(f"Digite o nome do aluno {i + 1} "))
        dados.append(nome)
        matricula = int(input(f"Digite a matricula do aluno {i + 1} "))
        dados.append(matricula)
        data = str(input(f"Digite a data de nascimento do aluno {i + 1} "))
        dados.append(data)
        matriz.append(dados[:])
        dados.clear()
    print("VALORES ADCIONADOS")
    print(matriz)


main()
