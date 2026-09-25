while True:
   
    print("""===================================
         SISTEMA DE GERENCIAMENTO
    ===================================""")

    usuario = input("Digite o seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if usuario == "admin" and senha == "123":
        print("\nLogin realizado com sucesso! Bem vindo, admin")
        input("ENTER para continuar...")


    print("""
========================================
                MENU
========================================
1 - Cadastrar usuário
2 - Listar usuários
3 - Alterar usuário
4 - Excluir usuário
5 - Logout
6 - Encerrar
========================================
""")


    opcao = input("Escolha uma opção: ")

    if opcao == 5:
                print("\nRealizando logout...")
                input("Pressione ENTER para continuar...")
                break

    elif opcao == 6:
                print("\nPrograma encerrado!")
               

    else:
                print("\nEssa opção ainda não está funcionando.")
                input("Pressione ENTER para continuar...")
else:
          print("\nUsuário ou senha incorretos!")
          input("Pressione ENTER para tentar novamente...")



print(" \033c", end="" """###############################################################################################
     BEM VINDO AO JOGO DE ADIVINHAÇÃO!!! AQUI VOCÊ TESTARÁ ACAPACIDADE DA SUA INTUIÇÃO.
     NIVEIS DE DIFICULDADE:
     1 = FÁCIL
     2 = MÉDIO
     3 = DIFÍCIL
################################################################################################### \n )""")
import random
while True:

    dificuldade = int(input("Digite sua escolha: "))

    if dificuldade == 1:
        limite = 10
    elif dificuldade == 2:
        limite = 20
    elif dificuldade == 3:
        limite = 30
    else:
        print("Opção inválida!")
        input("Pressione ENTER para continuar...")
        continue

    numero_sorteado = random.randint(1, limite)
    acertou = False

    print(f"\nVocê terá 3 chances para adivinhar um número de 1 a {limite}.")

    for tentativa in range(1, 4):
        numero = int(input(f"\nTentativa {tentativa}/3 - Digite seu palpite: "))

        if numero == numero_sorteado:
            print("Parabéns, você acertou!")
            acertou = True
            break

        print("Você errou!")

        if numero > numero_sorteado:
            print("Tente um número menor.")
        else:
            print("Tente um número maior.")

    if not acertou:
        print("\nVocê perdeu! Fim de jogo.")
        print(f"O número sorteado era {numero_sorteado}.")

    novamente = input("\nQuer jogar novamente? (s/n): ")

    if novamente != "s":
        print("\nObrigado por jogar!")
        break



