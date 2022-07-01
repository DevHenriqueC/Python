from time import sleep
n1 = float(input('Primeira nota:\n'))
n2 = float(input('Segunda nota:\n'))
resultado = (n1 + n2)/2
print('\033[1;35m')
print('Calculando...')
print('\033[m')
sleep(2)
print('A media do Aluno foi {} e ele está '.format(resultado))
if resultado > 7:
    print('\033[1;32m')
    print('-='*10)
    print('  Aprovado!!!')
    print('-='*10)
    print('\033[m')
elif resultado == 5 or 7:
    print('\033[1;33m')
    print('-='*10)
    print('  Em Recuperação!!!')
    print('-='*10)
    print('\033[m')
elif resultado < 5:
    print('\033[1;31m')
    print('-='*10)
    print('  Reprovado!!!')
    print('-='*10)
    print('\033[m')
