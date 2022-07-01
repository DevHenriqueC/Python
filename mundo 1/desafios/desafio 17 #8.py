from math import hypot
co = float(input('Digite o valor do cateto oposto.\n'))
ca = float(input('Digite o valor do cateto adjacent\n'))
h = hypot(co,ca)
print('A hipotenusa é igual a: {:.2f}'.format(h))
