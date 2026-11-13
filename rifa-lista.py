import random
lista = []
cadastro = input("digite o nome de quem comprou a rifa (clique ENTER quando terminar): ")
while cadastro:
    lista.append(cadastro)
    cadastro = input("digite o nome de quem comprou a rifa (clique ENTER quando terminar): ")
if len(lista) > 0: # "len()" serve para contar quantos elementos existem dentro de uma estrutura
    sorteado = random.randint(0, len(lista) - 1)
    print("Parabéns! O ganhador da rifa foi:", lista[sorteado])
else:
   
    print("parabéns! Este é o ganhador da rifa: ")
print(lista)
