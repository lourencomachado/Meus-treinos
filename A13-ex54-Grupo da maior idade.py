# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'em que ano a {pess}ª você nasceu: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f' Ao todo tivemos {totmaior} pessoas MAIORES DE IDADE.')
print(f' e também tivemos {totmenor} pessoas MENORES DE IDADE.')




