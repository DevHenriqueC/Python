casa = int(input('Qual o valor da casa?\n'))
salario = int(input('Qual o valor do seu salario?\n'))
anos = int(input('Em quantos anos você ira pagar?\n'))
prestacao = casa / (anos * 12)
print('A prestação por mes seria R${:.2f}'.format(prestacao))
if prestacao > salario*30/100:
    print('\033[1;31m','-='*20)
    print('Você não foi aceito para o emprestimo!!')
    print('-='*20, '\033[m')
elif prestacao < salario*30/100:
    print('\033[1;32m', '-='*20)
    print('Você foi aceito para fazer o emprestimo!!!')
    print('-='*20, '\033[m')

