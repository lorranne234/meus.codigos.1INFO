 import random
while True:

    print("\033c", end="")

    print("""
###############################################################################################
        BEM-VINDO AO JOGO DE ADIVINHAÇÃO!
        AQUI VOCÊ TESTARÁ A CAPACIDADE DA SUA INTUIÇÃO.

        NÍVEIS DE DIFICULDADE:
        1 = FÁCIL
        2 = MÉDIO
        3 = DIFÍCIL
###############################################################################################
""")

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

        numero = int(input(
            f"\nTentativa {tentativa}/3 - Digite seu palpite: "
        ))

        if numero == numero_sorteado:
            print("\nParabéns, você acertou!")
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

    novamente = input("\nQuer jogar novamente? (s/n): ").lower()

    if novamente != "s":
        print("\nObrigado por jogar!")
        break

