"""Crie uma agenda eletrônica que contenha dois vetores: um array com o nome dos seus amigos e outro com
as suas respectivas datas de aniversário. Tente inserir e remover as informações da agenda de maneira
dinâmica (apagando pelo nome ou posição, inserindo n usuários por vez caso queira, etc...). """


def menu():
    print(15 * "-", "AGENDA ELETRONICA", 15 * "-")
    print("1 - Inserir contatos\n"
          "2 - Remover contatos\n"
          "3 - Ver contatos\n"
          "4 - Sair\n")


def main():
    nomeAmigos = []
    dataAniversario = []
    menu()
    escolha = int(input("Oque voce deseja? [1,2,3,4]"))
    while escolha != 4:
        if escolha == 1:
            quantContatos = int(input("Quantos contatos você deseja adicionar? "))
            for i in range(quantContatos):
                nome = str(input("Qual o nome do contato que deseja adcionar? "))
                nomeAmigos.append(nome)
                data = str(input("Qual o numero do contato que deseja adicionar?"))
                dataAniversario.append(data)
            escolha = int(input("Oque voce deseja? [1,2,3,4]"))
        elif escolha == 2:
            if len(dataAniversario) == 0:
                print("AGENDA SEM VALORES")
                menu()
                escolha = int(input("Oque voce deseja? [1,2,3,4]"))
            else:
                deleteNome = str(input("Qual o nome do contato para exclusão? "))
                indexDelete = nomeAmigos.index(deleteNome)
                nomeAmigos.pop(indexDelete)
                dataAniversario.pop(indexDelete)
                menu()
                escolha = int(input("Oque voce deseja? [1,2,3,4]"))
        elif escolha == 3:
            print("1 - Contato por nome\n"
                  "2 - Todos os contatos salvos")
            escolha3 = int(input("Oque você deseja? [1, 2]"))
            if escolha3 == 1:
                cont = 0
                if len(dataAniversario) == 0:
                    print("AGENDA SEM VALORES")
                    menu()
                    escolha = int(input("Oque voce deseja? [1,2,3,4]"))
                else:
                    verAniversario = str(input("Qual o nome do contato? "))
                    for i in range(0, len(nomeAmigos)):
                        if nomeAmigos[i] == verAniversario:
                            indexAniversario = i
                            cont += 1
                            print(f"Seu amigo: {verAniversario} faz aniversaio em {dataAniversario[indexAniversario]}")
                            if cont > 1:
                                print(f"Voce tem mais de um amigo chamado {verAniversario}")
                    menu()
                    escolha = int(input("Oque voce deseja? [1,2,3,4]"))
            elif escolha3 == 2:
                for i in range(0, len(nomeAmigos)):
                    print(f"AMIGO: {nomeAmigos[i]} - DATA DE ANIVERSARIO: {dataAniversario[i]}")
                menu()
                escolha = int(input("Oque voce deseja? [1,2,3,4]"))


main()
