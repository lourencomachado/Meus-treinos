# faça um programa que mostre na tela uma contagem regressiva para
# o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 seg.entre elas.

# importando  biblioteca time
from time import sleep

# mensagem de início
print('\033[1mINICIANDO CONTAGEM REGRESSIVA\033[m ')

# criando laço for
for tempo in range(10, -1, -1):
    print(tempo)

# TEMPO DE ESPERA ENTRE OS NÚMEROS DA CONTAGEM
    sleep(1)

# mensagem de FIM
print('\033[1m kabum!!! pow! pow!\033[m')
