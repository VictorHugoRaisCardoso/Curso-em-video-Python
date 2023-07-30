from random import randint
from time import sleep

vitorias_consecutivas = int()

print("=" * 60)
print(f'{"Vamos Jogar Par ou Impar":^60}')
print("=" * 60)

while True:
    resultado = 0
    computador = randint(0,100)
    numero_do_jogador = int(input('Digite um número: '))
    escolha_do_jogador = str(input("Par ou Impar [P/I]: ")).upper()
    resultado = computador + numero_do_jogador
    
    if (escolha_do_jogador in 'P' or escolha_do_jogador in 'I'):
        if (resultado % 2 == 0 and escolha_do_jogador == 'P' or resultado % 2 != 0 and escolha_do_jogador == 'I'):
            print(f'Você jogou {numero_do_jogador} e o computador {computador}. Total de {resultado} DEU PAR')
            print(f'Você venceu!')
            vitorias_consecutivas += 1
        else:
            print(f'Você perdeu.')
            break
print(f'Você venceu por {vitorias_consecutivas} vezes consecutivas.')
