from time import sleep as sp
from random import randint as rd
jogo = []
sorteios = []
print("=" * 60)
print(f"{'JOGA NA MEGA SENA':^60}")
print("=" * 60)
quant = int(input("Quantos jogos você quer que eu sorteie? "))
print(f'{"-=-" * 6}    SORTEANDO   {quant} jogos {"-=-" * 6}')
while len(sorteios) != quant:
    while len(jogo) != 6:
        num = rd(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    sorteios.append(jogo[:])
    jogo.clear()
print(f"Os numeros sorteados foram: ")
sp(1)
for pos, i in enumerate(sorteios):
    print(f'Jogo {pos + 1}: {i}')
    sp(1)
print(f"{'-=-' * 8} < BOA SORTE > {'-=-' * 7}")
