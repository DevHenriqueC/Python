from time import sleep
leia = int(input('Me diga um numero de 0 a 1000.\n'))
print('Analizando banco de dados...')
sleep(2)
primos = 0
for c in range(2, leia):
    if leia % c == 0:
        print('Esse numero é multiplo de {}'.format(c))
        primos += 1

if primos == 0:
    print('Esse numero é primo.')
else:
    print('Esse numero não é primo.')



