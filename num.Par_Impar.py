numero = int(input("Digite o número que você deseja: "))

if numero % 2 == 0:
    resultado = numero ** 2
    print (f"O seu número é par, e o quadrado dele é: {resultado:.2f}")
else:
    resultado = numero ** 3
    print (f"O seu número é ímpar, e o cubo dele é: {resultado:.2f}")
