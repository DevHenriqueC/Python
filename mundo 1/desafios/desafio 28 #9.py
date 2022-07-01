from random import randint
from time import sleep

n = randint(0, 5)
a = int(input('Advinhe no numero que estou pensando. de 0 a 5.\n'))
print('Processando...')
sleep(2)
if a == n:
    print('Você ganhou!')
else:
    print('O numero que eu estava pensando era {}, e Você perdeu!'.format(n))
