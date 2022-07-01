v = float(input('Qual o valor do seu salario?\n'))
if v > 1250:
    print('Seu novo salario teve um aumento de 10% e será {}'.format(v+(v/100*10)))
else:
    print('Seu novo salario teve um aumento de 15% e será {}'.format(v+(v/100*15)))