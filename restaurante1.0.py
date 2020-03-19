# Lucas Rodrigues Fiori - 2019
# Inicio do programa
# Teclado padrao americano

clientes = int(input())
i_cons = int(input())
i = 0
pedidos_v = []
valor_v = []
total = 0
for i in range(0, i_cons):
    pedidos, valor = (input().split(" ", 1))  # separa o valor de pedidos e valor em uma linha

    valor_2 = int(valor)  # converte valor - str em valor2 - int

    ver = isinstance(pedidos, str)  # verifica se pedidos eh string
    ver_2 = isinstance(valor_2, int)  # verifica se valor_2 eh inteiro
    if ver is True:  # verifica se ver eh Verdadeiro, ou seja eh String
        pedidos_v.append(pedidos)  # adiciona dentro do array pedidos_v o valor de pedidos

    if ver_2 is True:  # verifica se ver eh Verdadeiro, ou seja inteiro
        valor_v.append(valor)  # adiciona dentro do array os valor_v os velores de valor

    total += int(valor)

    # FIM DO FOR#

retirar_1, retirar_2 = input().split(" ", 1)  # insere o nome dos produtos para retirar o valor

if retirar_1 in str(pedidos_v):  # verifica se o produto a ser retirado existe no array pedidos_v
    a = int(pedidos_v.index(retirar_1))  # se achou, ele pega o endereco onde esta o produto dentro do array

if retirar_2 in str(pedidos_v):  # se achou, ele pega o endereco onde esta o produto dentro do array
    b = int(pedidos_v.index(retirar_2))  # se achou, ele pega o endereco onde esta o produto dentro do array

retirar_valor_produto = valor_v[a] # vai no endereco, pega o valor que esta la dentro e armazena na variavel
retirar_valor_produto2 = valor_v[b] # vai no endereco, pega o valor que esta la dentro e armazena na variavel

total_a_retirar = int(retirar_valor_produto) + int(retirar_valor_produto2) # soma o total a se retirar

total_ja_retirado = total - total_a_retirar #retira o valor que tem que ser retirado

para_cada = total_ja_retirado / clientes # preco para cada cliente

print(total) # Printa o total da conta
print(total_ja_retirado) # Printa o que restou, ou seja o valor com os produtos ja retirado
print(para_cada) # O valor a ser pago por cliente