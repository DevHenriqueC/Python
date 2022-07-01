r1 = float(input('Me diga o seguimento.\n'))
r2 = float(input('Me diga o seguimento.\n'))
r3 = float(input('Me diga o seguimento.\n'))

#Se pode ou não formar um triangulo

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:

    #todos lados iguais

    if r1 == r2 == r3 and r2 == r1 == r3 and r3 == r1 == r2:
        print('Os seguimentos podem formar um TRIANGULO EQUILÁTERO.')

    #todos lados diferentes

    elif r1 != r2 != r3 != r1:
        print('Os seguimentos podem formar um TRIANGULO ESCALENO.')

    # dois lados iguais

    else:
        print('Os seguimentos podem formar um TRIANGULO ISÓSCELES.')

#Se nao formam triangulo

else:
    print('Os seguimentos não formam um TRIANGULO.')
