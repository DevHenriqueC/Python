p = int(input('Qual o preço do produto? '))
pc = int (input ('Esta em quantos "%" em promo? '))
s = p -(p/100*pc)
print('O produto ficara em R${}'.format(s))