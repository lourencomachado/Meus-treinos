print('''    \033[1;30;47m Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” \033[m
\033[1;30;47m em um número entre 0 e 10. Só que agora o                             \033[m
\033[1;30;47m jogador vai tentar adivinhar até acertar, mostrando                  \033[m
\033[1;30;47m no final quantos palpites foram necessários para vencer:             \033[m''')

from random import randint

computador = randint(0, 10)

print('''\n\033[1;33mSou seu computador....Acabei de pensar em um número de 0 a 10...\033[m
 \033[1;33m     Será que você consegue adivinhar qual número foi?:        \033[m''')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('\n\033[1;36m Qual é o seu palpite?: '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[1;36m Mais...Tente de Novo.\033[m')
        else:
            print('\033[1;36m MENOS...Tente Novamente!\033[m')

print(f'\n\033[1;32m Acertou com {palpites} tentativas.\033[m')

