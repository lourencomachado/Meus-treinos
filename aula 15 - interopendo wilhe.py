print('''Este código realiza a soma de uma série de números digitados pelo usuário.
    O loop continua até que o usuário digite o número 999, que é usado como condição de parada.
 A cada iteração, o número digitado é adicionado ao total ‘s’, e quando o loop é interrompido, 
 o programa imprime a soma dos números digitados, excluindo o número de parada 999.''')


print('Inicializa as variáveis n e s com o valor 0')

n = s = 0

# Cria um loop infinito
while True:
    # Solicita ao usuário que digite um número e armazena na variável n

    n = int(input('Digite um número: '))

    # Verifica se o número digitado é 999
    if n == 999:
        # Se for 999, interrompe o loop
        break

    # Se não for 999, adiciona o valor de 'n' ao total 's'
    s += n

# Após sair do loop, imprime o valor total acumulado em 's'
print(f'A soma vale {s}.')
