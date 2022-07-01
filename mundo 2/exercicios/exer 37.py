n = int(input('Escreva um numero para conversão:\n'))
print('[1] Binario')
print('[2] Octal')
print('[3] Hexadecimal')
c = int(input('Sua opção\n'))

if c == 1:
    print('O numero convertido pra Binario é: {}'.format(bin(n)[2:]))
elif c == 2:
    print('O numero convertido para Octal é: {}'.format(oct(n)[2:]))
elif c == 3:
    print('O numero convertido para Hexadecimal é: {}'.format(hex(n)[2:]))
else:
    print('Comando invalido.')

