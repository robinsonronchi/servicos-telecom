# Telecom - Usuário Telefone 2

## Desafio
Agora, vamos Adicionar uma funcionalidade à classe UsuarioTelefone para que possa ser verificado o saldo disponível em seu plano. Para essa solução, você pode criar uma classe PlanoTelefone, o seu método de inicialização e encapsular os atributos, 'nome' e 'saldo' dentro da classe. Adicione também um método 'verificar_saldo' para verificar o saldo do plano e uma  'mensagem_personalizada' para gerar uma mensagem personalizada.

### Condições da verificação do saldo:
- Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
- Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
- Caso contrário, retorne: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

### Entrada
Como entrada, será solicitado o nome, plano (Essencial, Prata, Premium) e saldo atual do cliente.

### Saída
Mensagem personalizada de acordo o saldo do cliente.

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
            João</br>
            Essencial</br>
            9
        </td>
        <td>
            Seu saldo está baixo. Recarregue e use os serviços do seu plano.
        </td>
        </tr>
        <tr>
        <td align="left">
            Debora</br>
            Prata</br>
            11
        </td>
        <td>
           Seu saldo está razoável. Aproveite o uso moderado do seu plano.
        </td>
        </tr>
        <tr>
        <td align="left">
            Catarina</br>
            Premium</br>
            50
        </td>
        <td>
            Parabéns! Continue aproveitando seu plano sem preocupações.
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