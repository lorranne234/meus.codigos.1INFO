lista = []
produto = input("informe o produto eletrônico que deseja (clique ENTER para parar): ")

while produto:
    lista.append(produto)
    produto = input("informe o produto eletrônico que deseja (clique ENTER para parar): ")
    mais = input("Quer adicionar mais algum produto? resoponda com (S/N) e ENTER para parar: ")
    if mais == "S":
        mais=input("informe o nome do produto: ")
    else:
        print(lista)
