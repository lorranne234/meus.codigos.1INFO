while True: #tradução "Enquanto verdadeiro"
    senha = int(input("senha: "))
    if senha == 12345:
        print ("Acesso liberado! ")
        break # traduçao "quebrar" para forçar a parada do loop. só coloco dentro if. se o if for verdadeiro o loop para.
    else:
        print("Tente novamente!!!")
