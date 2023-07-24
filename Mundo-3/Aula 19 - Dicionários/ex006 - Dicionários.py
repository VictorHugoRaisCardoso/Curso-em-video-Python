time = list()
partidas = list()
jogador = dict()
while True:
    jogador.clear()
    partidas.clear()
    jogador["nome"] = str((input('Nome do jogador: '))).title()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na {c + 1}ª partida? ')))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?[S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod  ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print(f"\n{'-' * 40}")
for k, v in enumerate(time):
    print(f'{k:^3}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostar os dados de qual jogador?(999 para encerrar): '))
    if busca == 999:
        print('<<< VOLTE SEMPRE >>>')
        break
    if busca >= len(time):
        print(f'ERRO! Não exite jogador {busca}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} --')
        for p, g in enumerate(time[busca]['gols']):
            print(f'No {p + 1}º jogo fez {g} gols.')
        print(f'Total de gols: {time[busca]["total"]}')
        print('-' * 40)
