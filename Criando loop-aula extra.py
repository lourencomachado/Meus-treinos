# percorrer uma lista
lista_produtos = ["faca", "garfo", "frigideira", "flavorstone"]
for produto in lista_produtos:
    print(produto.capitalize())
print(' ' * 20)
# Calcular imposto sobre vários valores
lista_precos = [10, 20, 200, 50, 300]
for preco in lista_precos:
    imposto = preco * 0.1
    print(imposto)
print(' ' * 20)
# percorrendo um dicionário
produtos = {"faca": 10,
            "garfo": 10,
            "panela": 200,
            "frigideira": 50,
            "flarvostone": 300,
            }
for produto in produtos:
    print(produto)
    print(produtos[produto])
print(' ' * 20)
# exemplo aplicado análise de vendas
# vendas no arquivo vendaslojas.txt
with open("vendasloja.txt", "r") as arquivo:
    texto = arquivo.read()
lista_texto = texto.split("\n")

faturamento = 0
# excluir a primeira linha
lista_texto = lista_texto[1:]
# para cada linha do meu arquivo
for linha in lista_texto:
    posicao_pv = linha.find(";")
    valor = float(linha[posicao_pv + 1:])
    faturamento += valor
print(faturamento)
