import sys

# Cria uma lista para armazenar os equipamentos
itens = []

# Loop para solicitar três equipamentos ao usuário
for i in range(3):
    # Solicita ao usuário um equipamento e armazena na variável "item"
    item = sys.stdin.readline().strip()  # Remove caracteres extras como '\n'
    
    # Adiciona o item à lista "itens"
    itens.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")  
# Loop para percorrer cada item na lista "itens"
for item in itens:
    print(f"- {item}")  # Imprime cada item com o prefixo '-'
