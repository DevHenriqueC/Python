v = int(input('Primeiro valor:\n'))
v1 = int(input('Segundo valor:\n'))
if v > v1:
    maior = v
    print('O maior numero é: {}'.format(maior))
elif v1 > v:
    maior = v1
    print('O maior numero é: {}'.format(maior))
elif v == v1:
    print('Não existe numero maior os numero {} e {} são iguais!!'. format(v, v1))
