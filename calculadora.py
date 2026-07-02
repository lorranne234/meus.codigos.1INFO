print("""calculadora simples
1. soma
2. subtração
3. multiplicação
4. divisão""")

opcao = int(input("Escolha a operação (1/2/3/4): "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == 1:
    resultado = num1 + num2
    print(f"O resultado da soma é: {num1 + num2}")
elif opcao == 2:
    resultado = num1 - num2
    print(f"O resultado da subtração é: {num1 - num2}")
elif opcao == 3:
    resultado = num1 * num2
    print(f"O resultado da multiplição é:{num1 * num2}")
elif opcao == 4:
    if num2 != 0:
        resultado = num1 / num2 
        print (f"O resultado da divisão é: {num1 / num2:.f}")
    else:
        print("Divisão por zero! escolha outro número!")
else:
    print("Opção inválida")
