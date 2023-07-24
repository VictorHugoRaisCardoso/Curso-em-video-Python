lista = []
aluno = []
num = 0
while True:
    aluno.append(str(input('Nome: ')).title())
    aluno.append(float(input('1ª Nota: ')))
    aluno.append(float(input('2ª Nota: ')))
    media = [(aluno[1] + aluno[2]) / 2]
    lista.append(aluno[:])
    lista[-1].insert(0, media)
    aluno.clear()
    sair = str(input('Quer cadastrar mais algum aluno? [S/N]: '))
    if sair in 'Nn':
        break
print("=" * 60)
print(f"No.  NOME                 MÉDIA")
print("_" * 60)
for pos, i in enumerate(lista):
    print(f'{pos:<4}{i[1]:<10}{i[0][0]:>17.1f}')
while True:
    print('_' * 31)
    num = int(input('Quer mostrar a nota de que aluno? (999 interrompe): '))
    if num == 999:
        print('FINALIZANDO...')
        break
    if num < len(lista):
        print(f'As notas de {lista[num][1]} são {lista[num][2:]}')
print('<<< VOLTE SEMPRE >>>')
