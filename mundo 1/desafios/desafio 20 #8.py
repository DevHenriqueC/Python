from random import shuffle
n = input('Diga o nome do 1° aluno:\n')
n1 = input('Diga o nome do 2° aluno:\n')
n2 = input('Diga o nome do 3° aluno:\n')
n3 = input('Diga o nome do 4° aluno:\n')
list = [n, n1, n2, n3]
shuffle(list)
print('A ondem é: {}'.format(list))
