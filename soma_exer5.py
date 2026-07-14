soma = 0
cont = 0
maior = 0
while True:
    num = int(input("Digite um número inteiro: "))
    if num <= 0:
        break
    soma += num
    cont += 1
    if num > maior:
        maior = num
print(f"a soma de todos os números positivos informados é: {soma}")
media_aritmetica = soma / cont
print(f"a média aritmética de todos os números positivos informados é: {media_aritmetica}")
print (f"O maior de todos os números informados é: {maior}")
