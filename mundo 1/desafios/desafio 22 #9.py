n = input('Qual seu nome? ').strip()
ss = n.split()

print('Seu nome todo em maiusculo é', n.upper())
print('Seu nome todo em minusculo é', n.lower())
print('Seu nome todo tem {} letras'.format(len(n) - n.count(' ')))
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))