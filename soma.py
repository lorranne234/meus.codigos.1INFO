soma = 0
while True:
    num = int(input("Digite um número inteiro: "))
    if num <= 0:
        break
    soma += num
print(f"a soma de todos os números positivos informados é: {soma}")
media_aritmetica = soma / num
print(f"a média aritmética de todos os números positivos informados é: {media_aritmetica}")
