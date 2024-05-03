import re
import sys

# Função para validar se um número de telefone está no formato correto
def validate_numero_telefone(phone_number):
    # Defina o padrão de expressão regular para o formato (XX) 9XXXX-XXXX
    pattern = r"\(\d{2}\) 9\d{4}-\d{4}"

    # Verifique se o número de telefone corresponde ao padrão
    if re.match(pattern, phone_number):
        # Se corresponder, o número é válido
        return "Número de telefone válido."
    else:
        # Se não corresponder, o número é inválido
        return "Número de telefone inválido."

# Solicita ao usuário que insira um número de telefone
phone_number = sys.stdin.readline().strip()  # Remove caracteres extras

# Chame a função 'validate_numero_telefone' com o número de telefone fornecido
result = validate_numero_telefone(phone_number)

# Imprime o resultado
print(result)
