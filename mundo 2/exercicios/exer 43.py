peso = float(input('Me fale qual o seu peso.(EM KG)\n'))
altu = float(input('Me fale qual sua altura.(EM METROS)\n'))
imc = peso / (altu ** 2)
print('Seu imc é {:.2f} e:'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do seu peso ideal.')
elif imc <= 25:
    print('Você está no seu peso ideal.')
elif imc <= 30:
    print('Você esta sobrepeso.')
elif imc <= 40:
    print('Você esta com obesidade cuidado!!!')
else:
    print('Você esta com obesidade morbida procure um medico!!')
