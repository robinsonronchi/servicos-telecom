class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        # Inicializa os atributos da classe
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano
    
    # Método especial para representação em string do objeto
    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."

# Entrada de dados do usuário
nome = input()
numero = input()
plano = input()

# Cria um novo objeto UsuarioTelefone com os dados fornecidos
usuario = UsuarioTelefone(nome, numero, plano)

# Imprime a mensagem indicando que o usuário foi criado com sucesso
print(usuario)
