from random import choice
a =  input('Me diga o nome do 1° aluno:\n')
a1 = input('Me diga o nome do 2° aluno:\n')
a2 = input('Me diga o nome do 3° aluno:\n')
a3 = input('Me diga o nome do 4° aluno:\n')
nomes = [a, a1, a2, a3]
s = choice(nomes)
print('O nome do Aluno sorteado é: {}'.format(s))







