a = str(input('Me fale uma palavra. ')).strip()
c = a.upper().find('A')+1
ct = a.upper().count('A')
f = a.upper().rfind('A')+1
print('A palavra tem {} letras "A"'.format(ct))
print('A letra A na palavra comeca em: {}'.format(c))
print('A letra A na palavra termina em: {}'.format(f))