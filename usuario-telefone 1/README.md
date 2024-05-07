# Telecom - Usuário Telefone 1

## Desafio
Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone. Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe. Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado, neste desafio, simulamos três planos, sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.

### Entrada
Nome do usuário, número de telefone e plano.

### Saída
Mensagem indicando que o usuário foi criado com sucesso.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

<table>
    <thead>
        <tr align="left">
        <th>Entrada</th>
        <th>Saída</th>
        </tr>
    </thead>
    <tbody align="left">
        <tr>
        <td align="left">
            Ana</br>
            (11) 91111-1111</br>
            Plano Essencial Fibra
        </td>
        <td>
            Usuário Ana criado com sucesso.
        </td>
        </tr>
        <tr>
        <td align="left">
            Sofia</br>
            (22) 92222-2222</br>
            Plano Prata Fibra
        </td>
        <td>
           Usuário Sofia criado com sucesso.
        </td>
        </tr>
        <tr>
        <td align="left">
            Pedro</br>
            (33) 93333-3333</br>
            Plano Premium Fibra
        </td>
        <td>
            Usuário Pedro criado com sucesso.
        </td>
        </tr>
    </tbody>
    <tfoot></tfoot>
</table>

## Dicas

Todas as entradas e saída dos algoritmos são utilizados o STDIN e STDOUT de cada linguagem, abaixo tem algumas dicas de como utilizar cada STDIN e STDOUT de cada linguagem.

### Python
Em Python existe várias formas de implementar o STDIN e STDOUT recomendamos utilizar sys.stdin.readline para o STDIN e o print para o STDOUT.

### Exemplo:
import sys
a = int(sys.stdin.readline()) // Lê a linha de entrada
print(a); // Imprime o dado
