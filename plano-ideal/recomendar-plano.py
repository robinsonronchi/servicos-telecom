import sys

# Função para recomendar o plano ideal baseado no consumo médio mensal
def recomendar_plano(consumo_medio):
    # Verifica qual plano é mais adequado para o consumo informado
    if consumo_medio <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo_medio <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"

# Solicita ao usuário que insira o consumo médio mensal de dados em GB
consumo = float(sys.stdin.readline())  # Lê a entrada do usuário
#consumo = float(input())

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado
print(recomendar_plano(consumo))  # Imprime o plano recomendado
