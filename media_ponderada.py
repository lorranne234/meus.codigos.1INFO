print("Apenas números positivos!")
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

print(""" 
1. média ponderada com pesos 2 e 3
2. Quadrado da soma dos 2 números
3. Cubo do menor número""")

opcao = int(input("Escolha a opção (1/2/3):"))

if opcao == 1:
    resultado = (num1 * 2 + num2 * 3) / 5
    print(f"o resultado da media ponderada destes números é {resultado:.2f}")
elif opcao == 2:
    resultado = (num1 + num2) ** 2
    print(f"o resultado do quadrado da soma dos dois números é {resultado:.2f}")
elif opcao == 3:
    if num1 > num2:
        resultado = num2 ** 3 
        print(f"O resultado do cubo menor é {resultado:.2f}")
    else: 
        resultado = num1 ** 3
        print(f"O resultado do menor número é {resultado:.2f}")
else:
    print("OPÇÃO INVÁLIDA!!!")
