
from time import sleep
r1 = float(input('Me diga o Seguimento: \n'))
r2 = float(input('Me diga o Seguimento: \n'))
r3 = float(input('Me diga o Seguimento: \n'))
print('\033[1;35mAnalizando...\033[m')
sleep(2)
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('\033[1;32m-=' * 21)
    print('Os seguimentos podem formar TRIANGULOS.')
    print('-=' * 21)
else:
    print('\033[1;31m-=' * 21)
    print('Os seguimentos não podem formar TRIANGULOS.')
    print('-=' * 21)
