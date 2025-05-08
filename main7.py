import os

mensagens = []

nome = input("Nome: ")

while True:

    #Limpando terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

     print("______________")

     # Obtendo texto 
     texto = input("mensagens: ")
  if texto == "FIM":
    break

  # adicionando mensagem na lista
   mensagens.append  