# Telecom - Usuário Telefone 3

## Desafio
Vamos agora, adicionar uma funcionalidade à classe UsuarioTelefone, que realizar chamadas para outros usuários. Cada chamada terá uma duração em minutos e o custo será deduzido do saldo do usuário, suponha o custo de $0.10 por minuto. Você pode criar um método fazer_chamada que vai permitir que o usuário faça a chamada, ele vai receber o destinatario e duracao como parâmetros. Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano', além de adicionar o método deduzir_saldo para deduzir o valor do saldo do plano e depois retorne uma mensagem adequada como mostra no exemplo a baixo.

### Entrada
Número do usuário, número do telefone, saldo inicial, número do destinatário e a duração da chamada em minutos.

### Saída
Mensagem indicando o sucesso da chamada ou saldo insuficiente para fazer a chamada.

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
            Rodrigo</br>
            (00) 90000-0000</br>
            10.00</br>
            (33) 93333-3333</br>
            60
        </td>
        <td>
            Chamada para (33) 93333-3333 realizada com sucesso. Saldo: $4.00
        </td>
        </tr>
        <tr>
        <td align="left">
            Yule</br>
            (11) 91111-1111</br>
            30.00</br>
            (00) 90000-0000</br>
            240
        </td>
        <td>
           Chamada para (00) 90000-0000 realizada com sucesso. Saldo: $6.00
        </td>
        </tr>
        <tr>
        <td align="left">
            Amelia</br>
            (33) 93333-3333</br>
            10.00</br>
            (11) 91111-1111</br>
            120
        </td>
        <td>
            Saldo insuficiente para fazer a chamada.
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
