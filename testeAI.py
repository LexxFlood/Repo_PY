# Função para calcular a média de uma lista
def calcular_media(numeros):
    return sum(numeros) / len(numeros)

# Lista de números pré-definidos
numeros = [10, 20, 30, 40, 50]  # Você pode alterar os números aqui

# Calcular a média
media = calcular_media(numeros)

# Classificar os números como acima ou abaixo da média
acima_da_media = []
abaixo_da_media = []

for numero in numeros:
    if numero > media:
        acima_da_media.append(numero)
    elif numero < media:
        abaixo_da_media.append(numero)
    else:
        pass  # Ignorar se o número for igual à média

# Exibir os resultados
print(f"Números fornecidos: {numeros}")
print(f"Média: {media:.2f}")
print(f"Acima da média: {acima_da_media}")
print(f"Abaixo da média: {abaixo_da_media}")
