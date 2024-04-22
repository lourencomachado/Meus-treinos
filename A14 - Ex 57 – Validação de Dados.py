# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

print('\033[1;30;47mSolicita ao usuário que informe o sexo e armazena a primeira letra em maiúscula:\033[m')

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

print('\033[1;30;47mEnquanto o valor fornecido não for M ou F, pede ao usuário para informar novamente:\033[m')

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]

print('\033[1;30;47mQuando um valor válido é fornecido, imprime uma mensagem de sucesso\033[m')

print('Sexo {} registrado com sucesso'.format(sexo))
