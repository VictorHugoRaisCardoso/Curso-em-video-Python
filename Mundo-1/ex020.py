import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
show = [n1, n2, n3, n4]
random.shuffle(show)
print(f'A sequência de alunos que irá apresentar é a seguinte: ')
print(show)
