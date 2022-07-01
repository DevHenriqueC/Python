from datetime import date
a = int(input('Qual ano quer analisar? Coloque 0 para analizar o ano que você esta.\n'))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('-=-' * 10)
    print('O ano {} é bissexto'.formart(a))
    print('-=-' * 10)
else:
    print('-=-' * 10)
    print('O ano {} não é bissexto.'.format(a))
    print('-=-'*10)
