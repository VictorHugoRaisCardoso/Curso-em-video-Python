jogador={}
gols = []
tot = int()
jogador['nome'] = str(input('Nome do jogador: '))
qt = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))
for i in range(0, qt):
    gols.append(int(input(f'   Quantidade de gols na {i+1}ª partida: ')))
    tot += gols[i]
jogador["gols"] = gols[:]
jogador["total"] = tot
print('=' * 60)
print(jogador)
print('=' * 60)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('=' * 60)
print(f'O jogador {jogador["nome"]} jogou {qt} partidas.')
for i in range(0, qt):
    print(f'Na partida {i+1}, fez {jogador["gols"][i]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
