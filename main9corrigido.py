def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True:
    try:
        # Entrada de valores
        valor1 = int(input("Valor 1: "))
        valor2 = int(input("Valor 2: "))
        
        # Chamando a função
        resultado = minha_funcao(valor1, valor2)
        print(f"{valor1} + {valor2} = {resultado}")
        
        # Opção para sair do loop
        sair = input("Deseja continuar? (s/n): ").strip().lower()
        if sair == 'n':
            print("Encerrando o programa...")
            break
    except ValueError:
        print("Por favor, insira apenas números inteiros.")
