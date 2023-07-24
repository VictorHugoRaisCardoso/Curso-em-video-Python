pessoa = list()
geral = list()
maior = list()
menor = list()
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    geral.append(pessoa[:])
    pessoa.clear()
    sair = str(input('Quer continuar? [S/N]: '))
    if sair in 'Nn':
        break
print(f'Ao todo foram cadastradas {len(geral)} pessoas.')
c = 0
for i in geral:
    if c == 0:
        for p in i:
            maior.append(p)
            menor.append(p)
            c += 1
    else:
        if maior[1] < i[1]:
            maior.clear()
            for p in i:
                maior.append(p)
        elif maior[1] == i[1]:
            for p in i:
                maior.append(p)
        if menor[1] > i[1]:
            menor.clear()
            for p in i:
                menor.append(p)
        elif menor[1] == i[1]:
            for p in i:
                menor.append(p)
print(f'As pessoas mais pesadas são {maior}')
print(f'As pessoas mais leves são {menor}')
