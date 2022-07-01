soma = 0
for c in range(0, 6):
    num = int(input('Digite um numero.'))
    par = num % 2
    if par == 0:
        soma += num
print('A soma de todos os numeros pares é {}'.format(soma))
