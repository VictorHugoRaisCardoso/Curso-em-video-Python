RG = list()
mulheres = list()
maior_media = list()
pessoa = dict()
maior = menor = media = int()
while True:
    pessoa['nome'] = str(input('Nome: ').title())
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite apenas "M" ou "F".')
    pessoa['idade'] = int(input('Idade: '))
    RG.append(pessoa.copy())
    while True:
        sair = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if sair in "SN":
            break
        print('ERRO! Digite apenas "S" ou "N".')
    if sair in 'N':
        break
for pos, i in enumerate(RG):
    if pos == 0:
        maior = menor = i['idade']
    else:
        if i['idade'] > maior:
            maior = i['idade']
        elif i['idade'] < menor:
            menor = i['idade']
media = (maior + menor) / 2
for i in RG:
    if i['sexo'] in 'F':
        mulheres.append(i.copy())
for i in RG:
    if i['idade'] > media:
        maior_media.append(i.copy())
print("=" * 60)
print(f'Ao todo foram cadastradas {len(RG)} pessoas.')
print(f'A idade média das pessoas é de {media} anos.')
print(f'Ao todo foram cadastradas {len(mulheres)} mulheres: ')
for i in mulheres:
    print(f"{i['nome']} ", end='')
print()
print('Pessoas que estão cadastradas acima da média: ')
for i in maior_media:
    print(f'Nome = {i["nome"]}; Sexo = {i["sexo"]}; Idade = {i["idade"]}')
