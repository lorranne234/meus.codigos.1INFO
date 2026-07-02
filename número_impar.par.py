numero = int(input("Digite o seu número inteiro:"))

if numero % 2==0:
    resultado = numero **2
    print (f"O seu número é par. E o quadrado do número é {resultado:.2f}")
else:
    resultado = numero **3
    print (f" O seu número é ímpar. E o cubo do número é {resultado:.2f}")
