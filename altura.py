a1 = float(input("Digite a primeira altura: "))
a2 = float(input("Digite a segunda altura: "))
a3 = float(input("Digite a terceira altura: "))

if a1 == a2 or a1 == a3 or a2 == a3:
    print("Há, pelo menos, 2 pessoas com a mesma estatura")
elif a1 > a2 and a1 > a3:
    print(f"Maior estatura é: {a1:.2f}")
elif a2 > a1 and a2 > a3:
    print(f"Maior estatura é: {a2:.2f}")
else: 
    print(f"Maior estatura é: {a3:.2f}")


