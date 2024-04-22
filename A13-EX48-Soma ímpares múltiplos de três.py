# Calcule a soma entre todos os números ímpares que são múltiplos
# de três e que se encontram no intervalo de 1 até 500.

# criando acumulador soma
soma = 0

# criando a variável contador
contador = 0

# laço for
for c in range(1, 501, 2):
    if c % 3 == 0:  # se ao dividir o número por 3 ele for igual a 0, ele é divisível por 3
        contador += 1  # define quantos números divisíveis por 3 tem entre os números solicitados no FOR.
        soma += c  # soma dos números divisíveis por 3 ENTRE OS NÚMEROS SOLICITADOS.
# RESULTADO NA TELA
print(f' a soma de todos os {contador} valores solicitados é {soma}')
