("""cargo e aumento.
Programador de sistemas - 30% de aumento.
Analistas de sistemas - 20% de aumento.
Analista de banco de dados - 15% de aumento.""")

cargo = input("Digite o cargo do funcionário: ")
salario = float(input("Digite o salário do seu funcionário: "))

if cargo == "Programador de sistemas":
    salario = salario + (salario * 0.30)
    print (f"O novo salário do seu funcionário é:{salario:.2f} ")
elif cargo == "Analistas de sistemas":
    salario = salario + (salario * 0.20)
    print (f"O novo salário do seu funcionário é:{salario:.2f} ")
elif cargo == "Analista de banco de dados":
    salario = salario + (salario * 0.15)
    print (f"O novo salário do seu funcionário é:{salario:.2f} ")
else:
    print("Cargo inválido!!!")
