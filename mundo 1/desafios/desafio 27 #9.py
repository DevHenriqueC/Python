n = str(input('Digite seu nome: ')).strip()
n1 = n.split()
print('Primeiro nome: {}'.format(n1[0]))
print('Ultimo nome: {}'.format(n1[len(n1)-1]))
