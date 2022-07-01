v = int(input('Qual é a distancia da sua viagem?\n***EM KM/H***\n'))
if v <= 200:
    print('-=-' * 10)
    print('Sua viagem vai ficar em {:.2f}'.format(v*0.50))
    print('-=-' * 10)
if v > 200:
    print('-=-' * 10)
    print('Sua viagem vai ficar em {:.2f}'.format(v*0.45))
    print('-=-' * 10)

    