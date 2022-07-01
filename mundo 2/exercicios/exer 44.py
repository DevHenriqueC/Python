print('{:=^40}'.format(' Lojas Henrique '))
preco = int(input('Qual o preço das compras?\n'))
met = int(input('Qual o metodo de pagamento?\n1-Dinheiro/Cheque 2-Cartão\n'))
if met == 1:
    print('O valor do produto ficara em {}'.format(preco-(preco/100*10)))
elif met == 2:
    cart = int(input('Vai dividir o produto em quantas vezes?\n'))
    if cart == 1:
        print('O valor do produto ficara em {}'.format(preco-(preco/100*5)))
    elif cart == 2:
        print('O valor do produto ficara em {}'.format(preco))
    elif cart >= 3:
        print('O valor do produto ficara em {}'.format(preco+(preco/100*20)))
else:
    print('Não conhecemos esse comando por favor digite um comando valido.')

