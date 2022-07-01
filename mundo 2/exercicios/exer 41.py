from datetime import date

ano = int(input('Em que ano o Atleta nasceu?\n'))
anoe = date.today().year
idade = anoe - ano

#Se o atleta tiver ate 9 anos

if idade <= 9:
    print('O atleta tem {} anos e se encontra na seleção Mirim!!'.format(idade))

#Se o atleta tiver entre 10 a 14

elif idade <=14:
    print('O atleta tem {} anos e se encontra na seleção Infantil!!'.format(idade))

#Se o atleta tiver entre 15 a 19

elif idade <=19:
    print('O atleta tem {} anos e se encontra na seleção Junior!!'.format(idade))

#Se o atleta tiver entre 19 a 20

elif idade <= 25:
    print('O atleta tem {} anos e se encontra na seleção Sênior!!'.format(idade))

#Se o atleta tiver mais de 20 anos

else:
    print('O atleta tem {} anos e se encontra na seleção Master!!'.format(idade))
    print('\033[1;32mParabens por chegar até aqui!!')
