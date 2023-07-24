from random import randint as ran
from operator import itemgetter
from time import sleep
rank = []
jogadores = {
    "jogador1" : ran(1, 6),
    "jogador2" : ran(1, 6),
    "jogador3" : ran(1, 6),
    "jogador4" : ran(1, 6)}
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f"{'== RANKING DOS JOGADORES ==': ^32}")
for pos, chave in enumerate(rank):
    print(f'O {pos + 1}º colocado foi o {chave[0]}: {chave[1]}')
    sleep(1)
