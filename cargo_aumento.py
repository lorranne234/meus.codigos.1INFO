""" FORMA DE PAGAGAMENTO:
1. À vista (em espécie) 15%
2. Cartão de débito 10%
3. Cartão de crédito (vencimento) 5%"""
forma_de_pagamento = int(input ("Digite a forma de pagamento, de acordo com as opções 1/2/3  : "))

total = float(input("Digite o valor total da venda: "))

if forma_de_pagamento == 1:
    desconto = (total - (total * 0.15))
    print (f"O valor final a ser pago é: {desconto:.2f} ")
elif forma_de_pagamento == 2:
    desconto = (total - (total * 0.10))
    print (f"O valor final a ser pago é: {desconto:.2f} ")
elif forma_de_pagamento == 3:
    desconto = (total - (total * 0.05))
    print (f"O valor final a ser pago é: {desconto:.2f} ")
