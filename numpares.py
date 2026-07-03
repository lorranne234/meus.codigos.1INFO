pares = 0
for i in range (10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares +=1
print(f"Foram informados {pares} números pares.")
