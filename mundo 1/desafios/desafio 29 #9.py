v = int(input('Você estava em quantos km/h ? \n'))
if v > 80:
    print('-=-' * 10)
    print('Você foi mutado em: R${:.2f}'.format((v-80)*7))
    print('-=-' * 10)
else:
    print('-=-' * 17)
    print('Parabens! Você não foi mutado. Dirija com segurança.')
    print('-=-' * 17)
