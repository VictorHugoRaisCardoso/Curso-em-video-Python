n = str(input('Informe o nome Completo do funcionário: ')).strip().title()
nome = n.split()
print(f'{n} cadastrado com sucesso!')
salario = float(input(f'Qual é o salário atual de {nome[0]} {nome[-1]}? R$'))
aumento = float(input(f'Em quantos % será aumentado o salário de {nome[0]}? '))
salario_atual = salario + (salario * aumento / 100)
print(f'{nome[0]} recebia R${salario:.2f}, com {aumento:.0f}%, passa a receber R${salario_atual:.2f}.')