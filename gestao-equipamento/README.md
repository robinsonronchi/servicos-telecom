<h1>Telecom - Plano Ideal</h1>

<h2>Desafio</h2>
Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos.

<h3>Entrada</h3>
O programa solicitará ao usuário que insira uma lista com três equipamentos para adicionar a rede.

<h3>Saída</h3>
Após a entrada dos itens, o programa exibirá a lista de equipamentos inseridos pelo usuário. Cada equipamento será listado com um prefixo ( - ) de marcação para melhor organização.

<h3>Exemplos</h3>
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

### Equipamentos
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
            Antena</br>
            Roteador</br>
            Switch
        </td>
        <td>
            Lista de Equipamentos:</br>
            - Antena</br>
            - Roteador</br>
            - Switch
        </td>
        </tr>
        <tr>
        <td align="left">
            Servidor</br>
            Cabinet Rack</br>
            Access Point
        </td>
        <td>
            Lista de Equipamentos:</br>
            - Servidor</br>
            - Cabinet Rack</br>
            - Access Point
        </td>
        </tr>
        <tr>
        <td align="left">
            Edge Routers</br>
            Patch Cord</br>
            UPS
        </td>
        <td>
            Lista de Equipamentos:</br>
            - Edge Routers</br>
            - Patch Cord</br>
            - UPS
        </td>
        </tr>
    </tbody>
    <tfoot></tfoot>
</table>

<h2>Dicas</h2>
Todas as entradas e saída dos algoritmos são utilizados o STDIN e STDOUT de cada linguagem, abaixo tem algumas dicas de como utilizar cada STDIN e STDOUT de cada linguagem.

<h3>Python</h3>
Em Python existe várias formas de implementar o STDIN e STDOUT recomendamos utilizar sys.stdin.readline para o STDIN e o print para o STDOUT.

<h3>Exemplo:</h3>
import sys
a = int(sys.stdin.readline()) // Lê a linha de entrada
print(a); // Imprime o dado
