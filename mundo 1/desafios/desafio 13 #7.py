s = float(input ('Qual seu salario? '))
a = int(input ('Quantos "%" subiu do seu salario? '))
t = s + (s/100*a)

print('Seu salario com {}% de desconto irá para: R${}'.format(a,t))