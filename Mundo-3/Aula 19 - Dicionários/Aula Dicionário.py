estado = dict()
brasil = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade federativa: '))
    estado['Sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
