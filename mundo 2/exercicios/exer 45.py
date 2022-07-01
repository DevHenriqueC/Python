from random import randint
from time import sleep

game = randint(1, 3)
joga = str(input('Escolha entre Pedra, Papel e Tesoura\n'))
jogad = joga.lower()

if game == 1:
    mente = 'pedra'
elif game == 2:
    mente = 'papel'
elif game == 3:
    mente = 'tesoura'

#empate

if jogad == 'pedra' and mente == 'pedra' or jogad == 'papel' and mente == 'papel' or jogad == 'tesoura' and mente == 'tesoura':
    print('Empatamos nos dois escolhemos {}'.format(mente))

#jogador ganha

if jogad == 'pedra' and mente == 'tesoura' or jogad == 'papel' and mente == 'pedra' or jogad == 'tesoura' and mente == 'papel':
    print('Você ganhou eu escolhi {}'.format(mente))

#maquina ganha

if mente == 'pedra' and jogad == 'tesoura' or mente == 'papel' and jogad == 'pedra' or mente == 'tesoura' and jogad == 'papel':
    print('Eu ganhei pois escolhi {}'.format(mente))
else:
    print('Não entendi esse comando por favor coloque um comando valido.')