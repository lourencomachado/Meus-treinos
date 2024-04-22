for c in range(0, 6):
    print('oi')
print('FIM')

print(' '*20)

for c in range(0, 6):
    print(c)

print(" "*20)

for c in range(6, 0, -1):
    print(c)

print(' '*20)

n = int(input('digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')

print(' '*20)

i = int(input('início: '))
f = int(input('fim: '))
p = int(input('passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
print(' '*20)
s = 0
for c in range(0, 4):
    n = int(input('digite um valor: '))
    s += n
print(f'o somatório de todos os valores é {s}')



